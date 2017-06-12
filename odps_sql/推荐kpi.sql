--@extra_input=
--odps sql 
--********************************************************************--
--@ author:利元
--@ create time:2017-04-27 13:50:38
--@ 上线管理: **每次上线需做变更说明, 管理员才能发布**
--@ v1.0: 变更说明 | 变更时间
--********************************************************************--


use ytsoku;

create table if not exists  ads_soku_app_sum_lovely_rec_di
(
    device_flag	 string comment '终端',
	app_ver		 string comment '版本',
	vdo_length	 string comment '视频长度',
	sqv_lovely   string comment '猜你喜欢搜索量',	
	click        string comment '点击量',
	click_vv	 string comment '点击播放量',
	vv     		 string comment '播放页首播vv',
	ts     		 string comment '播放页首播ts'
	--exp_rate     bigint comment '曝光率：exposure/sqv',
	--click_rate   bigint comment '点击率：click/exposure',
	--valid_click_per   bigint comment '单次搜索有效点击量：click_vv/click'
)
COMMENT '搜库_搜索结果页_猜你喜欢汇总数据'
partitioned by 
(
ds             string comment '日期'
)
LIFECYCLE 30;




insert overwrite table ads_soku_app_sum_lovely_rec_di partition (ds) 

select 
	device_flag,
	app_ver,
	vdo_length,
	sqv_lovely,
	click,
	click_vv,
	vv,
	ts,
	ds
from 
	(select 
		os_name  device_flag,    --设备终端
		app_ver,
		'total' vdo_length,
		count(*) click,																--猜你喜欢点击量及搜索量
		sum(if(spmd in ('poster', 'title', 'screenshot','language', 'playbutton', 'selectlist','selectbutton'),1,0)) click_vv,
		cast(count(distinct str_to_map(args, ',', '=') ['aaid']) as string) sqv_lovely,
		'0' vv,
		'0' ts,
		ds
	from ytcdm.dwd_yt_log_wl_app_clk_di 
	where ds='${ds}'
		and site = 'youku'
		and (app_ver >= '5.10.3' and dev_type='phone')
		and coalesce(split(spm_id, '\\.')[0]) = 'a2h0c' --所有搜索业务
		and concat(spma,'.',spmb,'.',spmc)='a2h0c.8166622.rlovely'
	group by os_name, 
		app_ver,
		ds
	
	union all
	
	
	select
		y1.device_flag,
		y1.app_ver,
		y1.vdo_length,
		y1.click,
		y1.click_vv,
		'0' sqv_lovely,
		cast(y2.vv as string) vv,
		cast(y2.ts as string) ts,
		y1.ds
	from 
		(select 
			a.device_flag,
			a.app_ver,
			case when c.vdo_len>1200 then 'long_vdo'
			else 'short_vdo' end vdo_length,
			sum(a.click) click,
			sum(a.click_vv) click_vv,
			a.ds
		from 
			(
			select 
				os_name  device_flag,    --设备终端
				app_ver,
				str_to_map(args, ',', '=')['object_id'] vdo_code,
				count(*) click,															--猜你喜欢点击量及搜索量
				sum(if(spmd in ('poster', 'title', 'screenshot','language', 'playbutton', 'selectlist','selectbutton'),1,0)) click_vv,
				ds
			from ytcdm.dwd_yt_log_wl_app_clk_di 
			where ds='${ds}'
				and site = 'youku'
				and (app_ver >= '5.10.3' and dev_type='phone')
				and coalesce(split(spm_id, '\\.')[0]) = 'a2h0c' --所有搜索业务
				and concat(spma,'.',spmb,'.',spmc)='a2h0c.8166622.rlovely'
			group by os_name, 
				app_ver,
				str_to_map(args, ',', '=')['object_id'],
				ds
			)a
			left outer join 

			(select 
				vdo_code vdo_code,
				vdo_id   object_id_inner,
				vdo_len,
				show_code,
				show_name,
				show_id,
				'1' type
			from 
				ytcdm.dim_yt_vdo
			where 
				ds = '${ds}' and site = 'youku' 
			union all 
			select 
				show_code vdo_code,
				cast(show_id as string)   object_id_inner,
				show_total_len*60 vdo_len,
				show_code,
				show_name,
				show_id,
				'2' type
			from 
				ytcdm.dim_yt_show
			where 
				ds = '${ds}' and site = 'youku' 
			) c 
			on a.vdo_code=c.vdo_code	
			where c.vdo_code is not null
		group by a.device_flag,
			a.app_ver,
			case when c.vdo_len>1200 then 'long_vdo'
			else 'short_vdo' end,
			a.ds
		)y1
		left outer join
		(
		select 
			t1.device_flag,
			t1.app_ver,
			case when t1.vdo_len>1200 then 'long_vdo'
			else 'short_vdo' end vdo_length,
			count(*) vv,
			sum(t1.ts) ts,
			t1.ds
		from 	
			(
			select 
				os_name device_flag,    --设备终端
				split(str_to_map(args, ',', '=')['vvlink'], '\\"')[3] aaid,
				a.*,
				row_number() over (partition by ds,split(str_to_map(args, ',', '=')['vvlink'], '\\"')[3] order by server_time asc)  ranknum
			from ytcdm.dwd_yt_log_wl_app_vv_di a
			where ds='${ds}' 
				and site = 'youku' 
				and split(url_spm_id, '\\.')[0] = 'a2h0c'
				and str_to_map(args, ',', '=')['vvlink'] is not null
				and str_to_map(args, ',', '=')['vvlink'] like '%aaid%'
				and split(str_to_map(args, ',', '=')['vvlink'], '\\"')[3]>20
				and (app_ver >= '5.10.3' and dev_type='phone' )	
				and ut_event_id = 12003 
				and (ts>0 and ts<86400)
			)t1
			left outer join 
			(
			select 
				a.aaid,
				a.device_flag,
				a.app_ver,
				a.click,
				a.click_vv,
				a.ds
			from 
			(
			select 
				os_name device_flag,    --设备终端
				app_ver,
				count(*) click,															--猜你喜欢点击量及搜索量
				sum(if(spmd in ('poster', 'title', 'screenshot','language', 'playbutton', 'selectlist','selectbutton'),1,0)) click_vv,
				str_to_map(args, ',', '=') ['aaid'] aaid
				,ds
			from ytcdm.dwd_yt_log_wl_app_clk_di 
			where ds='${ds}'
				and site = 'youku'
				and (app_ver >= '5.10.3' and dev_type='phone')
				and coalesce(split(spm_id, '\\.')[0]) = 'a2h0c' --所有搜索业务
				and concat(spma,'.',spmb,'.',spmc)='a2h0c.8166622.rlovely'
			group by os_name, 
				app_ver,
				str_to_map(args, ',', '=') ['aaid'],
				ds
				)a
			)t2
			on t1.device_flag=t2.device_flag
			and t1.app_ver=t2.app_ver
			and t1.ds=t2.ds
			and t1.aaid=t2.aaid
			where t2.aaid is not null
				and t1.ranknum=1

			group by t1.device_flag,
					t1.app_ver,
					case when t1.vdo_len>1200 then 'long_vdo'
					else 'short_vdo' end, 
					t1.ds
		)y2

		on y1.device_flag=y2.device_flag
		and y1.app_ver=y2.app_ver
		and y1.ds=y2.ds
		and y1.vdo_length=y2.vdo_length

)t

		





--select vdo_length,sum(sqv_lovely),sum(click_vv),sum(vv),sum(ts) from ytsoku.ads_soku_app_sum_lovely_rec_di where ds=20170507 group by vdo_length;

--select * from ytsoku.ads_soku_app_sum_lovely_rec_di where ds=20170507 limit 10;














	