--odps sql 
--********************************************************************--
--@ author:恩驰
--@ create time:2017-03-14 17:41:58
--@ 上线管理: **每次上线需做变更说明, 管理员才能发布**
--@ v1.0: 变更说明 | 变更时间
--********************************************************************--

use ytsoku;
create table if not exists ads_soku_app_abtest_search_query_overall_dev
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


insert overwrite table ads_soku_app_abtest_search_query_overall_dev partition (ds, device_flag, type)
select 
    expid_abd dim_var,
    '-1' dim_var1,
    '-1' dim_var2,
    'sqv' dim_name,
    sqv dim_value,
	ds,
    device_flag,
    'ogc_sqv' type
from 
(select 
    ds,
    concat(split(expid, '\\.')[0], '.', split(expid, '\\.')[1], '.',  split(expid, '\\.')[3]) expid_abd,
    count(distinct args['aaid']) sqv,
    'app_all' device_flag
from 
    (select 
    	a.*,
    	case when concat(os_name, '_', dev_type) = 'Android_phone'   then 'android_phone'
    		 when concat(os_name, '_', dev_type) = 'Android_pad'     then 'android_pad'
    		 when concat(os_name, '_', dev_type) = 'iPhone OS_phone' then 'ios_phone'
    		 when concat(os_name, '_', dev_type) = 'iPhone OS_pad'   then 'ios_pad'
    	else 'other' end  device_flag,
    	regexp_replace(split(regexp_replace(args['engine'], '\\$', '\\=', 0), '=')[1], 'rv', '', 0) expid,
    	lower(trim(split(a.spm_id,"\\.")[0])) spm_a,
    	lower(trim(split(a.spm_id,"\\.")[1])) spm_b,
    	lower(trim(split(a.spm_id,"\\.")[2])) spm_c,
    	lower(trim(split(a.spm_id,"\\.")[3])) spm_d	
    from 
    	ytsoku.dwd_soku_app_query_click_utsdk_log_di a 
    where 
    	ds = '${ds}' and args['aaid'] is not null 
    ) a 
group by 
	ds,
	concat(split(expid, '\\.')[0], '.', split(expid, '\\.')[1], '.',  split(expid, '\\.')[3])
union all 
select 
    ds,
    concat(split(expid, '\\.')[0], '.', split(expid, '\\.')[1], '.',  split(expid, '\\.')[3]) expid_abd,
    count(distinct args['aaid']) sqv,
    device_flag
from 
    (select 
    	a.*,
    	case when concat(os_name, '_', dev_type) = 'Android_phone'   then 'android_phone'
    		 when concat(os_name, '_', dev_type) = 'Android_pad'     then 'android_pad'
    		 when concat(os_name, '_', dev_type) = 'iPhone OS_phone' then 'ios_phone'
    		 when concat(os_name, '_', dev_type) = 'iPhone OS_pad'   then 'ios_pad'
    	else 'other' end  device_flag,
    	regexp_replace(split(regexp_replace(args['engine'], '\\$', '\\=', 0), '=')[1], 'rv', '', 0) expid,
    	lower(trim(split(a.spm_id,"\\.")[0])) spm_a,
    	lower(trim(split(a.spm_id,"\\.")[1])) spm_b,
    	lower(trim(split(a.spm_id,"\\.")[2])) spm_c,
    	lower(trim(split(a.spm_id,"\\.")[3])) spm_d	
    from 
    	ytsoku.dwd_soku_app_query_click_utsdk_log_di a 
    where 
    	ds = '${ds}' and args['aaid'] is not null 
    ) a 
group by 
	ds,
	concat(split(expid, '\\.')[0], '.', split(expid, '\\.')[1], '.',  split(expid, '\\.')[3]),
	device_flag
) un 
where un.expid_abd is not null
;

-- select * from ytsoku.ads_soku_app_abtest_search_query_overall_dev limit 10;