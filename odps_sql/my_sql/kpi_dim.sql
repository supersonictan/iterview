--odps sql 
--********************************************************************--
--@ author:泽彧
--@ create time:2017-05-04 23:36:16
--@ 上线管理: **每次上线需做变更说明, 管理员才能发布**
--@ v1.0: 变更说明 | 变更时间
--********************************************************************--
--select sum(vdo_clk)  from ads_soku_kpi_clk_dev where expid_abd='req.ugcn2.rank111' and exp_qp='all' and ds='${ds}';
--select sum(sqv) from ads_soku_kpi_sqv_dev where expid_abd='req.ugcn2.rank111' and exp_qp='all' and ds='${ds}';
--select sum(sqv) from ads_soku_kpi_sqv_dev where expid_abd='req.ugcn2.rank112' and exp_qp='all' and ds='${ds}';
--select *  from ads_soku_kpi_ctr_dev where ds='${ds}' and exp_qp='qa3' and expid_abd='req.ugcn2.rank112' and query='秦时明月之君临天下';
--select * from ads_soku_kpi_stats where ds='${ds}' and expid_abd='req.ugcn2.rank112' and query='铁齿铜牙纪晓岚第1部' order by sqv desc;











-------------------Start clk-------------------
CREATE TABLE IF NOT EXISTS ads_soku_kpi_clk_dev(
	expid_abd		STRING  COMMENT 		"实验ID",
	exp_qp			STRING 	COMMENT 		"实验走的QP,全部的是all",
	query			STRING 	COMMENT 		"query",
	vdo_clk			DOUBLE 	COMMENT 		"点击量"
) PARTITIONED BY(ds string) LIFECYCLE 30;

--计算query维度的点击量
INSERT OVERWRITE TABLE ads_soku_kpi_clk_dev PARTITION(ds)
--根据qa分类
SELECT 
	concat(split(expid, '\\.')[0], '.', split(expid, '\\.')[1], '.',  split(expid, '\\.')[3]) expid_abd
	,split(expid, '\\.')[4] exp_qp
	,args['k'] query
	,count(*) vdo_clk
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
	,split(expid, '\\.')[4]
	,args['k']
	,ds
UNION ALL
--不分qa
SELECT
	concat(split(expid, '\\.')[0], '.', split(expid, '\\.')[1], '.',  split(expid, '\\.')[3]) expid_abd
	,'all' exp_qp
	,args['k'] query
	,count(*) vdo_clk
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
--------------End clk-----------------


--drop table if exists ads_soku_kpi_sqv_dev;
-------------------Start sqv-------------
CREATE TABLE IF NOT EXISTS ads_soku_kpi_sqv_dev(
	expid_abd		STRING  COMMENT 		"实验ID",
	exp_qp			STRING 	COMMENT 		"实验走的QP,全部的是all",
	query			STRING 	COMMENT 		"query",
	sqv				DOUBLE 	COMMENT 		"sqv"
) PARTITIONED BY(ds string) LIFECYCLE 30;

INSERT OVERWRITE TABLE ads_soku_kpi_sqv_dev PARTITION(ds)
--分实验/qp统计
SELECT 
	concat(split(expid, '\\.')[0], '.', split(expid, '\\.')[1], '.',  split(expid, '\\.')[3]) expid_abd
	,split(expid, '\\.')[4]	exp_qp
	,args['k'] query
	,count(DISTINCT args['aaid']) sqv
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
	,split(expid, '\\.')[4]
	,ds
UNION ALL
--分实验，不分qp统计
SELECT 
	concat(split(expid, '\\.')[0], '.', split(expid, '\\.')[1], '.',  split(expid, '\\.')[3]) expid_abd
	,'all' exp_qp
	,args['k'] query
	,count(DISTINCT args['aaid']) sqv
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
--------------End sqv-----------------


-------------Start CTR------------------------
--drop table ads_soku_kpi_ctr_dev;
CREATE TABLE IF NOT EXISTS ads_soku_kpi_ctr_dev(
	expid_abd		STRING  COMMENT 		"实验ID",
	exp_qp			STRING 	COMMENT 		"实验走的QP,全部的是all",
	query			STRING 	COMMENT 		"query",
	ctr				DOUBLE  COMMENT 		"ctr"
) PARTITIONED BY(ds string) LIFECYCLE 30;

INSERT OVERWRITE TABLE ads_soku_kpi_ctr_dev PARTITION(ds)
SELECT
	clk.expid_abd expid_abd
	,clk.exp_qp
	,clk.query query
	,(clk.vdo_clk/sqv.sqv) ctr
	,clk.ds
FROM
(
	SELECT
		*
	FROM
		ads_soku_kpi_clk_dev
	WHERE
		ds='${ds}'
) clk
JOIN
(
	SELECT
		*
	FROM
		ads_soku_kpi_sqv_dev
	WHERE
		ds='${ds}'
) sqv
ON
	clk.query = sqv.query
	AND clk.expid_abd = sqv.expid_abd
	AND clk.exp_qp = sqv.exp_qp
;
----------------End CTR-------------





---------------Start Join（ctr关联sqv）------------
CREATE TABLE IF NOT EXISTS ads_soku_kpi_stats(
	expid_abd		STRING  COMMENT 		"实验ID",
	exp_qp			STRING 	COMMENT 		"实验走的QP,全部的是all",
	query			STRING 	COMMENT 		"query",
	sqv				DOUBLE 	COMMENT 		"搜索量",
	ctr				DOUBLE 	COMMENT 		"点击率"
) PARTITIONED BY(ds string) LIFECYCLE 30;

INSERT OVERWRITE TABLE ads_soku_kpi_stats PARTITION(ds)
SELECT 
	a.expid_abd expid_abd,
	a.exp_qp,
	a.query,
	a.sqv sqv,
	b.ctr ctr,
	a.ds ds
FROM 
(
	select * from ads_soku_kpi_sqv_dev where ds='${ds}'
) a
JOIN 
(
	select * from ads_soku_kpi_ctr_dev where ds='${ds}'
) b
ON 
	a.query = b.query
	AND a.expid_abd = b.expid_abd
	AND a.exp_qp = b.exp_qp
-------------------End Join-----------------