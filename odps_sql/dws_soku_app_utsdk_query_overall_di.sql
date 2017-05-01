--odps sql 
--********************************************************************--
--@ author:恩驰
--@ create time:2016-11-03 16:48:13
--@ desc: 计算搜索sqv, dau等指标
--********************************************************************--
use ytsoku;
create table if not exists dws_soku_app_utsdk_query_overall_di
(
	dim_var string comment '搜索词',
	sqv int	comment '搜索量',
	dau int	comment '搜索用户数',
	epv int	comment '总点击量',
	hit_epv int	comment '命中点击量',
	hit_uv int	comment '命中用户数',
	sqv_si int	comment '搜索会话数',
	click_si int comment '点击会话数',
	click_vv int comment '视频点击量',
	click_uv int comment '视频点击人数' 
)
partitioned by (ds string,device_flag string,dim_name string)
lifecycle 90; 
 
 --汇总keywor_kpi
 insert overwrite table dws_soku_app_utsdk_query_overall_di partition (ds,device_flag,dim_name)
 select 
	 args['k'],
	 count(distinct if((args['aaid'] is not null or spm_id = 'a2h0c.8166619.kubox.search'), args['aaid'], null)) sqv ,
	 count(distinct if((args['aaid'] is not null or spm_id = 'a2h0c.8166619.kubox.search'), utdid, null)) dau,
	 sum(if((args['aaid'] is not null and logtype = '3'), 1, 0)) epv,
	 count(distinct if((args['aaid'] is not null and logtype = '3'), args['aaid'], null)) hit_epv,
	 count(distinct if((args['aaid'] is not null and logtype = '3'), utdid, null)) hit_uv,
	 count(distinct if((args['aaid'] is not null or spm_id = 'a2h0c.8166619.kubox.search'), se_id, null)) sqv_si,
	 count(distinct if((args['aaid'] is not null and logtype = '3'), se_id, null)) click_si,
	 sum(if(lower(trim(split(spm_id,"\\.")[3])) in ('poster', 'title', 'screenshot', 'playbutton', 'selectlist'),1,0)) click_vv,
	 count(distinct if(lower(trim(split(spm_id,"\\.")[3])) in ('poster', 'title', 'screenshot', 'playbutton', 'selectlist'),utdid,null)) click_uv,
	 ds,'app_all','all_keyword' 
 from 
 	ytsoku.dwd_soku_app_query_click_utsdk_log_di 
 where 
 	ds=${ds} 
 group by 
 	ds,args['k'];

 

 
 
 --利元增加comment信息，20170407
 
