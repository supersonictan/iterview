--odps sql 
--********************************************************************--
--@ author:利元
--@ create time:2017-03-14 17:30:07
--@ 上线管理: **每次上线需做变更说明, 管理员才能发布**
--@ v1.0: 变更说明 | 变更时间
--********************************************************************--

use ytsoku;
CREATE TABLE IF NOT EXISTS ads_soku_engine_abtest_bounce_rate
( 
    dim_var      STRING COMMENT '维度名称',
	dim_var1     STRING COMMENT '备用维度1',
	dim_var2     STRING COMMENT '备用维度2',
    dim_name     STRING COMMENT '指标名称',
    dim_value    BIGINT COMMENT '指标值'
)
PARTITIONED BY (
    ds          STRING COMMENT '统计日期',
	device_flag string comment '终端',
	type        STRING COMMENT '数据名称'
)
LIFECYCLE 90;


insert overwrite table ads_soku_engine_abtest_bounce_rate partition (ds, device_flag, type)
select 
    dim_var,
	'-1' dim_var1,
	'-1' dim_var2,
	dim_name,
	dim_value,
	ds, 
	device_flag,
	'abtest_bounce_rate' type 
from 
(
    select 
		 bi_udf:bi_explode_narray(ds, expid,device_flag,
		  concat(
						'pv'  
				 , ':', 'uv' 
				 , ':', 'session_cnt'    
				 , ':', 'sqv'  
				 , ':', 'click'
				 , ':', 'video_click'
				 , ':', 'hit_uv'
				 , ':', 'bounce_rate_u'
				 , ':', 'ctr'
				 ),  
		  concat(
						pv 
				 , ':', uv 
				 , ':', session_cnt    
				 , ':', sqv 
				 , ':', click
				 , ':', video_click
				 , ':', hit_uv
				 , ':', (bounce_rate_u*100000)
				 , ':', (ctr*100000)
				 ),   
		  ':', 2) as (ds, dim_var,device_flag, dim_name, dim_value)
    from 
        ytsoku.ads_soku_engine_abtest_bounce_rate_di 
	where 
		ds = '${ds}'

	   

)t

;