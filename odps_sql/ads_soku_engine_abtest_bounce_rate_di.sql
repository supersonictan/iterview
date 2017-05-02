--odps sql 
--********************************************************************--
--@ author:利元
--@ create time:2017-03-24 17:07:57
--@ 上线管理: **每次上线需做变更说明, 管理员才能发布**
--@ v1.0: 变更说明 | 变更时间
--********************************************************************--

use ytsoku;

create table if not exists ads_soku_engine_abtest_bounce_rate_di 
(
expid string comment '实验号',
pv bigint comment '搜索结果页page view',
uv bigint comment '搜索结果页uv',
session_cnt bigint comment '搜索结果页会话数',
sqv bigint comment '搜索量：独立aaid数量',
click bigint comment '点击量',
video_click bigint comment '播放点击量',
hit_uv bigint comment '命中用户数',
bounce_rate_u double comment '用户跳出率',
ctr double comment '点击率',
device_flag string comment '终端'
) comment '搜库abtest核心数据表测试'
partitioned by (ds string comment '分区日期')
lifecycle 35;



-- 基于pv日志计算pv uv session
insert overwrite table ads_soku_engine_abtest_bounce_rate_di partition (ds)
select 
    expid,
	pv,
	uv,
	session_cnt,
	sqv,
	click,
	video_click,
	hit_uv,
	bounce_rate_u,
	ctr,
	device_flag,
	ds
from 
(
	select 
		a.expid,
		'app_all' device_flag,
		a.pv,
		a.uv,
		a.session session_cnt,
		a.sqv,
		b.click,
		b.video_click,
		b.hit_uv,
		case when uv = 0 then 0 else round(1-hit_uv/uv, 4) end bounce_rate_u,
		case when pv = 0 then 0 else round(click/pv, 4) end ctr,
		a.ds
	from 
		(select 
			 ds
			,concat(split(engine,'\\.')[0],'.',split(engine,'\\.')[1],'.',split(engine,'\\.')[3]) expid
			,count(*) pv
			,count(distinct utdid) uv
			,count(distinct se_id) session
			,count(distinct args['aaid']) sqv
		from 
			(select 
				 a.*,
				 bi_udf:bi_key_value(args['engine'],'\\$','\\=','expid') engine
				from 
					ytsoku.dwd_soku_app_pv_utsdk_log_di a 
				where 
					ds = '${ds}' and 
					args['engine'] is not null 
					and split(spm_id,'\\.')[0] = 'a2h0c'
			 ) a 
		group by 
			ds,
			concat(split(engine,'\\.')[0],'.',split(engine,'\\.')[1],'.',split(engine,'\\.')[3])
		) a 
	-- 计算所有点击量 计算视频点击量
	join 
		(select 
			ds,
			concat(split(engine,'\\.')[0],'.',split(engine,'\\.')[1],'.',split(engine,'\\.')[3]) expid,
			sum(if(logtype = '3', 1, 0)) click,
			sum(if(spm_a = 'a2h0c' and spm_d in ('poster', 'title', 'screenshot', 'playbutton', 'selectlist'), 1, 0)) video_click,
			count(distinct(if(logtype = '3', utdid, null))) hit_uv
		from 
			(select 
				 a.*,
				 bi_udf:bi_key_value(args['engine'],'\\$','\\=','expid') engine,
				 lower(trim(split(a.spm_id,"\\.")[0])) spm_a,
				 lower(trim(split(a.spm_id,"\\.")[1])) spm_b,
				 lower(trim(split(a.spm_id,"\\.")[2])) spm_c,
				 lower(trim(split(a.spm_id,"\\.")[3])) spm_d
			 from 
				 ytsoku.dwd_soku_app_query_click_utsdk_log_di a 
			 where 
				 ds = '${ds}' and args['engine'] is not null 
			 ) b 
		group by 
			ds,
			concat(split(engine,'\\.')[0],'.',split(engine,'\\.')[1],'.',split(engine,'\\.')[3])
		) b 
	on a.ds = b.ds and a.expid = b.expid


	union all

	select 
		a.expid,
		a.device_type device_flag,
		a.pv,
		a.uv,
		a.session session_cnt,
		a.sqv,
		b.click,
		b.video_click,
		b.hit_uv,
		case when uv = 0 then 0 else round(1-hit_uv/uv, 4) end bounce_rate_u,
		case when pv = 0 then 0 else round(click/pv, 4) end ctr,
		a.ds
	from 
		(select 
			 ds
			,device_type
			,concat(split(engine,'\\.')[0],'.',split(engine,'\\.')[1],'.',split(engine,'\\.')[3]) expid
			,count(*) pv
			,count(distinct utdid) uv
			,count(distinct se_id) session
			,count(distinct args['aaid']) sqv
		from 
			(select 
				 a.*,
				 case when concat(os_name, '_', dev_type) = 'Android_phone' then 'android_phone'
					 when concat(os_name, '_', dev_type) = 'Android_pad' then 'android_pad'
					 when concat(os_name, '_', dev_type) = 'iOS_phone' then 'ios_phone'
					 when concat(os_name, '_', dev_type) = 'iOS_pad' then 'ios_pad'
				 else 'other' end device_type,
				 bi_udf:bi_key_value(args['engine'],'\\$','\\=','expid') engine
				from 
					ytsoku.dwd_soku_app_pv_utsdk_log_di a 
				where 
					ds = '${ds}' and 
					args['engine'] is not null 
					and split(spm_id,'\\.')[0] = 'a2h0c'
			 ) a 
		group by 
			ds,device_type,
			concat(split(engine,'\\.')[0],'.',split(engine,'\\.')[1],'.',split(engine,'\\.')[3])
		) a 
	-- 计算所有点击量 计算视频点击量
		join 
		(select 
			ds,
			device_type,
			concat(split(engine,'\\.')[0],'.',split(engine,'\\.')[1],'.',split(engine,'\\.')[3]) expid,
			sum(if(logtype = '3', 1, 0)) click,
			sum(if(spm_a = 'a2h0c' and spm_d in ('poster', 'title', 'screenshot', 'playbutton', 'selectlist'), 1, 0)) video_click,
			count(distinct(if(logtype = '3', utdid, null))) hit_uv
		from 
			(select 
				 a.*,
				 case when concat(os_name, '_', dev_type) = 'Android_phone' then 'android_phone'
					 when concat(os_name, '_', dev_type) = 'Android_pad' then 'android_pad'
					 when concat(os_name, '_', dev_type) = 'iPhone OS_phone' then 'ios_phone'
					 when concat(os_name, '_', dev_type) = 'iPhone OS_pad' then 'ios_pad'
				 else 'other' end device_type,
				 bi_udf:bi_key_value(args['engine'],'\\$','\\=','expid') engine,
				 lower(trim(split(a.spm_id,"\\.")[0])) spm_a,
				 lower(trim(split(a.spm_id,"\\.")[1])) spm_b,
				 lower(trim(split(a.spm_id,"\\.")[2])) spm_c,
				 lower(trim(split(a.spm_id,"\\.")[3])) spm_d
			 from 
				 ytsoku.dwd_soku_app_query_click_utsdk_log_di a 
			 where 
				 ds = '${ds}' and args['engine'] is not null 
			 ) b 
		group by 
			ds,
			device_type,
			concat(split(engine,'\\.')[0],'.',split(engine,'\\.')[1],'.',split(engine,'\\.')[3])
		) b 
		on a.ds = b.ds and a.expid = b.expid and a.device_type=b.device_type


)t



--参考表ads_soku_kmd_overall_kpi