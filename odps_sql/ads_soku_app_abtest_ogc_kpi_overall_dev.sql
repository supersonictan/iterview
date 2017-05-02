--odps sql 
--********************************************************************--
--@ author:恩驰
--@ create time:2017-03-14 17:41:58
--@ 上线管理: **每次上线需做变更说明, 管理员才能发布**
--@ v1.0: 变更说明 | 变更时间
--********************************************************************--

use ytsoku;
create table if not exists ads_soku_app_abtest_ogc_kpi_overall_dev
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


insert overwrite table ads_soku_app_abtest_ogc_kpi_overall_dev partition (ds, device_flag, type)
select 
    dim_var,
    dim_var1,
    dim_var2,
    dim_name,
    dim_value,
	ds,
    device_flag,
    type
from 
    (select * from ytsoku.ads_soku_app_abtest_search_query_overall_dev where ds = '${ds}' 
	 union all 
	 select * from ytsoku.ads_soku_app_abtest_ogc_click_overall_dev_show where ds = '${ds}'
	 union all 
	 select * from ytsoku.ads_soku_app_abtest_ogc_click_overall_dev_vdo where ds = '${ds}'
	 union all 
	 select * from ytsoku.ads_soku_engine_abtest_bounce_rate where ds = '${ds}'
	 ) a 
;

-- select * from ytsoku.ads_soku_app_abtest_search_query_overall_dev limit 10;