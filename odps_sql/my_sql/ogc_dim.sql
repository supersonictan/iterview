--odps sql 
--********************************************************************--
--@ author:泽彧
--@ create time:2017-05-17 11:16:47
--@ 上线管理: **每次上线需做变更说明, 管理员才能发布**
--@ v1.0: 变更说明 | 变更时间
--********************************************************************--



-------------------Start 筛选出ogc基础-------------------------
CREATE TABLE IF NOT EXISTS ads_soku_kpi_baseOGC_dev(
	ip                    STRING COMMENT 'IP：格式为如 192.169.1.1',
    guid                  STRING COMMENT 'GUID：GUID',
    utdid                 STRING COMMENT 'UTDID：utdid',
    server_time           STRING COMMENT '服务器收集时间：服务器收集时间',
    local_time            STRING COMMENT '客户端采集时间：客户端采集时间',
    se_id                 STRING COMMENT '会话ID：会话ID',
    clk_object_id         STRING COMMENT '控件ID：对应原refercode.内容id',
    clk_object_name       STRING COMMENT '控件名称：控件名称',
    pre_clk_object_name   STRING COMMENT '上一个控件名称(此字段暂时没有意义，请勿使用)',
    clk_object_num        STRING COMMENT '控件序号：对应原refercode.内容序号',
    clk_object_type       STRING COMMENT '控件内容类型：控件内容类型，对应原refercode.内容类型，和object_id配合使用',
    clk_object_title      STRING COMMENT '控件内容标题：如;papi酱逛家居店泣血体验',
    page                  STRING COMMENT '页面名称：页面名称',
    ut_event_id           BIGINT COMMENT 'UT事件ID：UT事件ID：2001 页面浏览 详见http://tbdocs.alibaba-inc.com/pages/viewpage.action?pageId=199471773',
    network               STRING COMMENT '网络类型：wifi;2G;3G;4G',
    mac                   STRING COMMENT 'MAC地址：终端的MAC地址',
    imei                  STRING COMMENT '移动设备国际身份码缩写：移动设备国际身份码缩写',
    idfa                  STRING COMMENT '广告标示符：广告标示符（IDFA-identifierForIdentifier）',
    os_name               STRING COMMENT '操作系统名称：操作系统名称如android,ios 等',
    os_ver                STRING COMMENT '操作系统版本：4.1;9.2',
    app_key               STRING COMMENT 'APPKEY：APPID 中@前面的数字',
    app_ver               STRING COMMENT '客户端版本：youku android:5.7.1; youku iphone:5.8',
    sdk_ver               STRING COMMENT 'SDK版本：APP SDK的版本',
    resolution            STRING COMMENT '分辩率：终端的分辨率,如1024X768',
    dev_type              STRING COMMENT '终端类型：phone/pad/tv/pc',
    dev_brand             STRING COMMENT '终端品牌：苹果;三星;小米',
    model_type            STRING COMMENT '机型：细分的机型，如P7，iphone5s',
    carrier               STRING COMMENT '电信运营商：电信运营商 carrier, 中国联通，中国移动，中国电信',
    country_name          STRING COMMENT '国家中文名称：国家中文名称：如中国、美国',
    province_name         STRING COMMENT '省份中文名称：省份中文名称：如北京、上海',
    city_name             STRING COMMENT '城市中文名称：城市中文名称：如 杭州、长沙',
    mbr_id                BIGINT COMMENT '会员ID：会员ID',
    mbr_name              STRING COMMENT '会员名称：会员名称',
    is_vip                STRING COMMENT '是否VIP会员：Y：是 N:否',
    sex                   STRING COMMENT '性别：0=女,1=男,2=保密',
    birthday              STRING COMMENT '生日：生日',
    vip_level             BIGINT COMMENT '会员级别：黄金、白银、其他',
    page_chnl_level1_id   BIGINT COMMENT '一级页面频道ID：一级页面频道ID',
    page_chnl_level1_name STRING COMMENT '一级页面频道名称：一级页面频道名称',
    page_chnl_level2_id   STRING COMMENT '二级页面频道ID：二级页面频道ID',
    page_chnl_level2_name STRING COMMENT '二级页面频道名称：二级页面频道名称',
    long_user_id          STRING COMMENT '长登录用户ID：长登录用户ID',
    spm_id                STRING COMMENT '控件SPM：点击位置的abcd位',
    scm_id                STRING COMMENT 'SCMID：SCM标识符',
    logkey                STRING COMMENT '日志请求串：如pv日志的/1.gif,黄金令箭日志的定位串 /sns.1.1,*.gif说明见：http://baike.corp.taobao.com/index.php/AliLog',
    pid                   STRING COMMENT '渠道ID：在每个应用商店中APP会有一个标识符，能够在应用商店中唯一标识这个APP以及APP适用的终端',
    args                  MAP<STRING, STRING> COMMENT '事件参数：事件参数，根据不同的点击事件类型传不同的参数',
	expid				  STRING COMMENT '实验ID',
	show_code			  STRING COMMENT '节目code',
	show_id			  	  STRING COMMENT '节目id',
	show_name			  STRING COMMENT '节目name'
) PARTITIONED BY(ds string) LIFECYCLE 30;

INSERT OVERWRITE TABLE ads_soku_kpi_baseOGC_dev PARTITION(ds)
SELECT 
	a.*
	,regexp_replace(split(regexp_replace(a.args['engine'], '\\$', '\\=', 0), '=')[1], 'rv', '', 0) expid,
	b.show_code AS show_code,
	b.show_id AS show_id,
	b.show_name AS show_name
FROM 
(
	SELECT
		*
	FROM
		ytsoku.dwd_soku_app_query_click_utsdk_log_di
	WHERE
		ds='${ds}'
		AND clk_object_type in ('1', '2', '3')
		AND lower(trim(split(spm_id, "\\.")[3])) in ('poster', 'title', 'screenshot', 'playbutton', 'selectbutton', 'selectlist')
		AND args['object_id'] is not null
		AND length(args['object_id']) >= 5
		AND length(args['object_id']) <= 25
) a
JOIN
(
	SELECT
		*
	FROM 
		ytcdm.dim_yt_show
	WHERE 
		ds='${ds}' and site='youku' and show_id is not null and show_code is not null
) b
ON 
	a.args['object_id'] = b.show_code;

-------------------End 筛选出ogc基础-------------------------













-------------------Start clk-------------------
CREATE TABLE IF NOT EXISTS ads_soku_kpi_ogc_clk_dev(
	expid_abd		STRING  COMMENT 		"实验ID",
	exp_qp			STRING 	COMMENT 		"实验走的QP,全部的是all",
	query			STRING 	COMMENT 		"query",
	ogc_clk			DOUBLE 	COMMENT 		"点击量"
) PARTITIONED BY(ds string) LIFECYCLE 30;

--计算query维度的点击量
INSERT OVERWRITE TABLE ads_soku_kpi_ogc_clk_dev PARTITION(ds)
--根据qa分类
SELECT 
	concat(split(expid, '\\.')[0], '.', split(expid, '\\.')[1], '.',  split(expid, '\\.')[3]) expid_abd
	,split(expid, '\\.')[4] exp_qp
	,args['k'] query
	,count(*) ogc_clk
	,ds ds
FROM 
(
	ads_soku_kpi_baseOGC_dev
) a
GROUP BY 
	concat(split(expid, '\\.')[0], '.', split(expid, '\\.')[1], '.',  split(expid, '\\.')[3])
	,split(expid, '\\.')[4]
	,args['k']
	,ds
UNION ALL
--分实验，分query，不分qa
SELECT
	concat(split(expid, '\\.')[0], '.', split(expid, '\\.')[1], '.',  split(expid, '\\.')[3]) expid_abd
	,'all' exp_qp
	,args['k'] query
	,count(*) vdo_clk
	,ds ds
FROM
(
	ads_soku_kpi_baseOGC_dev
) a
GROUP BY
	concat(split(expid, '\\.')[0], '.', split(expid, '\\.')[1], '.',  split(expid, '\\.')[3])
	,args['k']
	,ds
;
UNION ALL
----分实验，不分query，不分qa
SELECT
	concat(split(expid, '\\.')[0], '.', split(expid, '\\.')[1], '.',  split(expid, '\\.')[3]) expid_abd
	,'all' exp_qp
	,'all' query
	,count(*) vdo_clk
	,ds ds
FROM
	ads_soku_kpi_baseOGC_dev a
GROUP BY
	concat(split(expid, '\\.')[0], '.', split(expid, '\\.')[1], '.',  split(expid, '\\.')[3])
	,ds
;
--------------End clk-----------------