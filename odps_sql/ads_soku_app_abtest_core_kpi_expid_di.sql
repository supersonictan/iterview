--odps sql 
--********************************************************************--
--@ author:利元
--@ create time:2017-04-13 09:52:05
--@ 上线管理: **每次上线需做变更说明, 管理员才能发布**
--@ v1.0: 变更说明 | 变更时间
--********************************************************************--

use ytsoku;
create table if not exists ads_soku_app_abtest_core_kpi_expid_di
(
     expid  				string comment '实验号'
    ,sqv           			string comment '搜索量'
    ,ogc_click    			string comment '总OGC点击量'
	,ogc_click_uv			string comment '总OGC点击用户数'
    ,ogc_show     			string comment '节目OGC点击量'
    ,ogc_vdo       			string comment '视频OGC点击量'
    ,vdo_click     			string comment '总播放点击量'
	,vdo_click_uv			string comment '总播放点击用户数'
    ,search_valid_vv  		string comment '搜索有效vv'
    ,search_vv_ratio 		string comment '搜索转化率'
    ,rpo           			string comment '千次搜索OGC(点击量)'
    ,vdo_click_ratio 		string comment '播放点击率(单次搜索点击量)'
    ,ogc_click_ratio 		string comment 'OGC点击占(总点击)比'
    ,bounce_rate_u 			string comment '用户跳出率(有播放点击用户数(命中用户)/总搜索用户)'
    ,ctr 					string comment '视频点击率(click/pv)'
	,device_flag	 		string comment '设备终端'
) partitioned by 
(
	ds             string comment '日期'

) lifecycle 25;


insert overwrite table ads_soku_app_abtest_core_kpi_expid_di partition (ds)

select 
     
    a.expid
    ,a.sqv          
    ,a.ogc_click 
	,a.ogc_click_uv
    ,a.ogc_show      
    ,a.ogc_vdo       
    ,a.vdo_click 
	,a.vdo_click_uv
    ,a.search_valid_vv  
    ,a.search_vv_ratio 
    ,a.rpo           
    ,a.vdo_click_ratio 
    ,a.ogc_click_ratio 
    ,a.bounce_rate_u 
    ,a.ctr 
	,a.device_flag
	,a.ds 
from 
    (
    select
         a.dim_var expid
        ,a.sqv
        ,c.ogc_click
        ,c.ogc_click_uv
        ,c.ogc_show
        ,c.ogc_vdo
        ,c.vdo_click
        ,c.vdo_click_uv
        ,d.search_valid_vv 
        ,case when a.sqv=0 then null else round(d.search_valid_vv/ a.sqv,4) end search_vv_ratio        
        ,case when a.sqv=0 then null else round(c.ogc_click * 1000 / a.sqv, 2) end rpo
        ,case when a.sqv=0 then null else round(c.vdo_click / a.sqv, 4) end vdo_click_ratio
        ,case when c.vdo_click=0 then null else round(c.ogc_click/ c.vdo_click, 4) end ogc_click_ratio 
        ,round(b.bounce_rate_u/100000,4) bounce_rate_u
        ,round(b.ctr/100000,4) ctr
		,a.device_flag
		,a.ds
    from 
        (
            select 
                 substring(ds, 1, 10) ds
                ,dim_var
                ,sum(if(dim_name = 'sqv', dim_value, 0))  sqv
    			,device_flag
            from 
                ytsoku.ads_soku_app_abtest_ogc_kpi_overall_dev
            where 
                ds = '${ds}' 
                and type = 'ogc_sqv'
            group by 
                substring(ds, 1, 10)
                , dim_var
                ,device_flag
        ) a  
		left outer join 
		(
            select 
                 substring(ds, 1, 10) ds
                ,dim_var
                ,sum(if(dim_name = 'ogc_click', dim_value, 0))      ogc_click
                ,sum(if(dim_name = 'ogc_click_uv', dim_value, 0))   ogc_click_uv
                ,sum(if(dim_name = 'ogc_show', dim_value, 0))       ogc_show
                ,sum(if(dim_name = 'ogc_vdo', dim_value, 0))        ogc_vdo
                ,sum(if(dim_name = 'vdo_click', dim_value, 0))      vdo_click
                ,sum(if(dim_name = 'vdo_click_uv', dim_value, 0))   vdo_click_uv  
    			,device_flag
            from 
                ytsoku.ads_soku_app_abtest_overall_dev_di
            where 
                ds = '${ds}' 
                and type ='core_abtest_overall'
            group by substring(ds, 1, 10), dim_var,device_flag
        ) c 
		on a.ds=c.ds
        and a.dim_var=c.dim_var
		and a.device_flag=c.device_flag
		left outer join 
		(
            select 
                 substring(ds, 1, 10) ds
                ,dim_var
                ,sum(if(dim_name = 'search_vv', dim_value, 0))      search_vv 
                ,sum(if(dim_name = 'search_valid_vv', dim_value, 0))   search_valid_vv 
                ,sum(if(dim_name = 'search_ts', dim_value, 0))   search_ts  
    			,device_flag
            from 
                ytsoku.ads_soku_app_abtest_valid_vv_di
            where ds = '${ds}' 
                  and type ='core_abtest_overall'
            group by substring(ds, 1, 10), dim_var,device_flag
        ) d 
		on a.ds=d.ds
        and a.dim_var=d.dim_var
		and a.device_flag=d.device_flag
        left outer join
        (
            select 
                 substring(ds, 1, 10) ds
                ,dim_var
                ,sum(if(dim_name = 'bounce_rate_u', dim_value, 0))  bounce_rate_u
                ,sum(if(dim_name = 'ctr', dim_value, 0))  ctr
    			,device_flag
            from 
                ytsoku.ads_soku_engine_abtest_bounce_rate
            where ds = '${ds}' 
                  and type='abtest_bounce_rate'
            group by substring(ds, 1, 10), dim_var,device_flag
        ) b
        on a.ds=b.ds
        and a.dim_var=b.dim_var
		and a.device_flag=b.device_flag
    ) a 

;