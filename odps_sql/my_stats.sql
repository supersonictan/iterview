--odps sql 
--********************************************************************--
--@ author:泽彧
--@ create time:2017-04-30 08:52:02
--@ 上线管理: **每次上线需做变更说明, 管理员才能发布**
--@ v1.0: 变更说明 | 变更时间
--********************************************************************--
--select sum(value) from ytsoku_dev.ads_soku_kpi_analayse where ds=20170429 and expid_abd='req.ugcn2.rank111' and key_name='sqv';
--select sum(value) from ytsoku_dev.ads_soku_kpi_analayse where ds=20170429 and expid_abd='req.ugcn2.rank111' and key_name='vdo_click';


--实验搜索词维度分析
drop table if exists ads_soku_kpi_analayse;
CREATE TABLE IF NOT EXISTS ads_soku_kpi_analayse(
	expid_abd		STRING  COMMENT 		"实验ID",
	query			STRING 	COMMENT 		"query",
	key_name		STRING 	COMMENT 		"sqv\click\ogc_click",
	value			DOUBLE 	
	--args			MAP<STRING,STRING>		"sqv\click\ogc_click"
) PARTITIONED BY(ds string) LIFECYCLE 60;




--计算query维度的点击量
INSERT INTO TABLE ads_soku_kpi_analayse PARTITION(ds)
SELECT 
	concat(split(expid, '\\.')[0], '.', split(expid, '\\.')[1], '.',  split(expid, '\\.')[3]) expid_abd
	,args['k'] query
	,'vdo_click' key_name
	,count(*) value
	,ds ds
FROM 
(
	SELECT 
		a.*
		,regexp_replace(split(regexp_replace(args['engine'], '\\$', '\\=', 0), '=')[1], 'rv', '', 0) expid
	FROM 
		ytsoku.dwd_soku_app_query_click_utsdk_log_di a
	WHERE 
		ds='${ds}'
		AND clk_object_type in ('1', '2', '3')
		AND lower(trim(split(a.spm_id, "\\.")[3])) in ('poster', 'title', 'screenshot', 'playbutton', 'selectbutton', 'selectlist')
		AND args['object_id'] is not null
		AND length(args['object_id']) >= 5
		AND length(args['object_id']) <= 25
) a
GROUP BY 
	concat(split(expid, '\\.')[0], '.', split(expid, '\\.')[1], '.',  split(expid, '\\.')[3])
	,args['k']
	,ds
;
	
	
	

--计算query维度的sqv
INSERT INTO TABLE ads_soku_kpi_analayse PARTITION(ds)
SELECT 
	concat(split(expid, '\\.')[0], '.', split(expid, '\\.')[1], '.',  split(expid, '\\.')[3]) expid_abd
	,args['k'] query
	,'sqv'	key_name
	,count(DISTINCT args['aaid']) value
	,ds	ds
FROM 
(
	SELECT 
		a.*
		,regexp_replace(split(regexp_replace(args['engine'], '\\$', '\\=', 0), '=')[1], 'rv', '', 0) expid
	FROM 
		ytsoku.dwd_soku_app_query_click_utsdk_log_di a
	WHERE 
		ds='${ds}'
		AND args['aaid'] is not null 
) a
GROUP BY 
	concat(split(expid, '\\.')[0], '.', split(expid, '\\.')[1], '.',  split(expid, '\\.')[3])
	,args['k']
	,ds
;




--计算query维度的点击率
INSERT INTO TABLE ads_soku_kpi_analayse PARTITION(ds)
SELECT
	a.expid_abd expid_abd
	,a.query query
	,'ctr' key_name
	,(a.value/b.value) value
	,a.ds
FROM
(
	SELECT
		*
	FROM
		ads_soku_kpi_analayse
	WHERE
		key_name = 'vdo_click'
		AND ds='${ds}'
) a
JOIN
(
	SELECT
		*
	FROM
		ads_soku_kpi_analayse
	WHERE
		key_name = 'sqv'
		AND ds='${ds}'
) b
ON
	a.query = b.query
	AND a.expid_abd = b.expid_abd
;