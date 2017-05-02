--odps sql 
--********************************************************************--
--@ author:利元
--@ create time:2017-04-12 14:07:57
--@ 上线管理: **每次上线需做变更说明, 管理员才能发布**
--@ v1.0: 变更说明 | 变更时间
--********************************************************************--

--解析engine，并添加视频是否ogc标记。

use ytsoku;
CREATE TABLE IF NOT EXISTS dwd_soku_app_abtest_click_expid_ogc_di
(
    guid                  STRING COMMENT 'GUID：GUID',
    utdid                 STRING COMMENT 'UTDID：utdid',
    os_ver                STRING COMMENT '操作系统版本：4.1;9.2',
    app_key               STRING COMMENT 'APPKEY：APPID 中@前面的数字',
    app_ver               STRING COMMENT '客户端版本：youku android:5.7.1; youku iphone:5.8',
    sdk_ver               STRING COMMENT 'SDK版本：APP SDK的版本',
    model_type            STRING COMMENT '机型：细分的机型，如P7，iphone5s',
	device_type           STRING COMMENT '终端类型及操作系统：Android_phone/ios_phone/pad',
    spm_id                STRING COMMENT '控件SPM：点击位置的abcd位',
    scm_id                STRING COMMENT 'SCMID：SCM标识符',
	is_vip				  STRING COMMENT '是否VIP会员：Y：是 N:否',
	pid                   STRING COMMENT '渠道ID：在每个应用商店中APP会有一个标识符，能够在应用商店中唯一标识这个APP以及APP适用的终端',
    args                  MAP<STRING, STRING> COMMENT '事件参数：事件参数，根据不同的点击事件类型传不同的参数',
	engine				  MAP<STRING, STRING> COMMENT '搜索实验号',
	vvlink_aaid		      STRING COMMENT '搜索实验号对应的aaid',
	object_type		      STRING COMMENT '点击内容类型：1 视频 ；2 节目；21 话题；24 自频道；3 播单；4 URL；5 专题；10 现场首发和自频道直播；17 来疯个人房间',
	object_id		      STRING COMMENT '点击控件的内容ID：1视频vid；2节目showid；3播单的playlistid/视频id；4url地址；5专题id；10直播id;17来疯房间id；21话题id；24道长uid', 
	object_title		  STRING COMMENT '对应object_type和object_id的标题',
	channelid		      STRING COMMENT '视频结果所属的频道',
	group_id		      STRING COMMENT '点击控件的群组ID 容器id',
	k		      		  STRING COMMENT '用户输入搜索关键词:指发生点击时的k，是当前搜索结果的状态信息',
	isplay		      	  STRING COMMENT '点击是否为播放点击',
	is_ogc		     	  STRING COMMENT '1为ogc, 其他为0',
	show_code		      STRING COMMENT '媒资库关联的节目ID',
	show_name			  STRING COMMENT '媒资库关联的节目名称',
	ogc_type		      STRING COMMENT '点击的内容类型1为节目中的视频，2为节目'
	
)
COMMENT '搜库APP实验搜索与点击表-ABTEST'
PARTITIONED BY (
    ds                    STRING COMMENT '分区字段：账期，YYYYMMDD'
)
LIFECYCLE 35;


insert overwrite table dwd_soku_app_abtest_click_expid_ogc_di partition (ds)
select 
	guid,
	utdid,
	os_ver,
	app_key,
	app_ver,
	sdk_ver,
	model_type,
	device_type,
	spm_id,
	scm_id,
	is_vip,
	pid,
	args,
	str_to_map(engine, '\\$','\\=') engine, 
	aaid vvlink_aaid,
	object_type,
	object_id,
	object_title,
	channelid,
	group_id,
	k,
	isplay,
	is_ogc,
	show_code,
	show_name,
	ogc_type,
	ds
from 
	(select 
        a.*,
        if(b.object_id is not null, 1, 0) is_ogc,
		b.show_code,
		b.show_name,
		b.type ogc_type
		
    from 
		(	
		select 
			guid,
			utdid,
			os_ver,
			app_key,
			app_ver,
			sdk_ver,
			model_type,
			case when concat(os_name, '_', dev_type) = 'Android_phone' then 'android_phone'
				 when concat(os_name, '_', dev_type) = 'iPhone OS_phone' then 'ios_phone'
			 else 'other' end device_type,
			spm_id,
			scm_id,
			is_vip,
			pid,
			str_to_map(args, ',', '=') args,
			str_to_map(args, ',', '=')['engine'] engine,
			str_to_map(args, ',', '=')['aaid']  aaid,
			str_to_map(args, ',', '=')['object_type']  object_type,
			str_to_map(args, ',', '=')['object_id']  object_id,
			str_to_map(args, ',', '=')['object_title']  object_title,
			str_to_map(args, ',', '=')['channelid']  channelid,
			str_to_map(args, ',', '=')['group_id']  group_id,
			str_to_map(args, ',', '=')['k']  k,
			str_to_map(args, ',', '=')['isplay']  isplay,
			ds
		from 
			ytcdm.dwd_yt_log_wl_app_clk_di
		where 
			ds = '${ds}'  
			and site = 'youku'  -- 只取youku的数据
			and str_to_map(args, ',', '=')['engine'] is not null
			and str_to_map(args, ',', '=')['aaid'] is not null
			and (app_ver >= '5.10.3' and dev_type='phone' and os_name in ('iPhone OS','Android')) 
			and lower(trim(split(spm_id,"\\.")[0]))= 'a2h0c' -- 搜索结果页的spm.a标识(包括结果页及详情页等)
			
		)a
	 left outer join 
        (select 
            vdo_code object_id,
            vdo_id   object_id_inner,
        	show_code,
			show_name,
        	show_id,
    		'1' type
        from 
            ytcdm.dim_yt_vdo
        where 
            ds = '${ds}' and site = 'youku' and 
        	copyright = 'authorized' and show_id is not null
        union all 
        select 
            show_code object_id,
            cast(show_id as string)   object_id_inner,
        	show_code,
			show_name,
        	show_id,
    		'2' type
        from 
            ytcdm.dim_yt_show
        where 
            ds = '${ds}' and site = 'youku' and 
        	copyright = 'authorized' and show_id is not null
        ) b 
	on a.object_id = b.object_id
	) a
;


