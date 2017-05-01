--odps sql 
--********************************************************************--
--@ author:恩驰
--@ create time:2017-03-17 09:52:05
--@ 上线管理: **每次上线需做变更说明, 管理员才能发布**
--@ v1.0: 变更说明 | 变更时间
--********************************************************************--

use ytsoku;
create table if not exists ads_soku_app_abtest_overall_dev_di
(
    dim_var        string comment '',
    dim_var1       string comment '',	
    dim_var2       string comment '',	
	dim_name       string comment '',
	dim_value      bigint comment ''
) partitioned by 
(
	ds             string comment '',
	device_flag    string comment '',
	type           string comment ''
) lifecycle 25;


insert overwrite table ads_soku_app_abtest_overall_dev_di partition (ds, device_flag, type)
select 
     dim_var
    ,'-1' dim_var1
    ,'-1' dim_var2
    ,dim_name
    ,dim_value
	,ds
    ,device_flag
    ,type
from 
    (select 
    	bi_udf:bi_explode_narray(ds, device_flag, type, expid_abd,
    	  concat(
    				   'vdo_click'         
    			 ,':', 'vdo_click_uv' 
    			 ,':', 'ogc_click' 
    			 ,':', 'ogc_click_uv'  
    			 ,':', 'ogc_vdo' 
    			 ,':', 'ogc_show' 
    			 ),  
    	  concat(
    				   vdo_click         
    			 ,':', vdo_click_uv 
    			 ,':', ogc_click
    			 ,':', ogc_click_uv  
    			 ,':', ogc_vdo 
    			 ,':', ogc_show 
    			 ),  
    	  ':', 2) as (ds, device_flag, type, dim_var, dim_name, dim_value)
        
    from 
        (select 
             expid_abd
        	,'-1' dim_var
        	,count(*) vdo_click
        	,count(distinct utdid) vdo_click_uv
        	,sum(if(is_ogc = '1', 1, 0)) ogc_click
    		,count(distinct (if(is_ogc = '1', utdid, ''))) ogc_click_uv
        	,sum(if(is_ogc = '1' and ogc_type = '1', 1, 0)) ogc_vdo
        	,sum(if(is_ogc = '1' and ogc_type = '2', 1, 0)) ogc_show
        	,ds
        	,'app_all' device_flag
        	,'core_abtest_overall' type
        from 
            ytsoku.dwd_soku_app_query_click_abtest_log_di
        where 
            ds = '${ds}' and expid_abd is not null 
        group by 
            expid_abd,
        	ds 
        union all 
        select 
             expid_abd
        	,'-1' dim_var
        	,count(*) vdo_click
        	,count(distinct utdid) vdo_click_uv
        	,sum(if(is_ogc = '1', 1, 0)) ogc_click
    		,count(distinct (if(is_ogc = '1', utdid, ''))) ogc_click_uv
        	,sum(if(is_ogc = '1' and ogc_type = '1', 1, 0)) ogc_vdo
        	,sum(if(is_ogc = '1' and ogc_type = '2', 1, 0)) ogc_show
        	,ds
        	,device_flag
        	,'core_abtest_overall' type
        from 
            ytsoku.dwd_soku_app_query_click_abtest_log_di
        where 
            ds = '${ds}' and expid_abd is not null 
        group by 
            expid_abd,
        	ds,
        	device_flag
        ) a 
	) b ;
