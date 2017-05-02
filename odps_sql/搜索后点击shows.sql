--odps sql 
--********************************************************************--
--@ author:泽彧
--@ create time:2017-05-02 11:20:36
--@ 上线管理: **每次上线需做变更说明, 管理员才能发布**
--@ v1.0: 变更说明 | 变更时间
--********************************************************************--
SELECT
	show_name
	,show_id
	,expid_abd
	,query
	,count(show_id) cnt
	--,vdo_code
FROM
(
	SELECT
		b.show_name
		,b.show_id
		,concat(split(a.expid, '\\.')[0], '.', split(a.expid, '\\.')[1], '.',  split(a.expid, '\\.')[3]) expid_abd
		,a.args['k'] query
		,a.args['object_id'] vdo_code
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
	JOIN
	(
		SELECT vdo_code,show_id,show_name FROM ytcdm.dim_yt_vdo WHERE ds='${ds}'
	) b
	ON
		a.args['object_id'] = b.vdo_code
) a
WHERE
	a.query='乡村爱情9全集免费版全集2017'
	AND a.expid_abd='req.ugcn2.rank110'
GROUP BY
	show_name
	,show_id
	,expid_abd
	,query
ORDER BY
	cnt