--odps sql 
--********************************************************************--
--@ author:恩驰
--@ create time:2016-11-02 18:23:25
--@ desc: dwd_soku_app_query_click_utsdk_log_di
--********************************************************************--

CREATE TABLE IF NOT EXISTS ytsoku.dwd_soku_app_query_click_utsdk_log_di
(
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
    args                  MAP<STRING, STRING> COMMENT '事件参数：事件参数，根据不同的点击事件类型传不同的参数'
)
COMMENT '搜库APP搜索与点击表'
PARTITIONED BY (
    ds                    STRING COMMENT '分区字段：账期，YYYYMMDD', 
    site                  STRING COMMENT '分区字段：站点，youku，tudou，来疯, other',
	logtype               STRING COMMENT '0:搜索日志， 1：点击日志')
LIFECYCLE 365;


insert overwrite table ytsoku.dwd_soku_app_query_click_utsdk_log_di partition (ds, site, logtype)
select 
     ip              
    ,guid            
    ,utdid           
    ,server_time     
    ,local_time      
    ,se_id           
    ,clk_object_id   
    ,clk_object_name 
    ,pre_clk_object_name 
    ,clk_object_num  
    ,clk_object_type 
    ,clk_object_title 
    ,page            
    ,ut_event_id     
    ,network         
    ,mac             
    ,imei            
    ,idfa            
    ,os_name         
    ,os_ver          
    ,app_key         
    ,app_ver         
    ,sdk_ver         
    ,resolution      
    ,dev_type        
    ,dev_brand       
    ,model_type      
    ,carrier         
    ,country_name    
    ,province_name   
    ,city_name       
    ,mbr_id          
    ,mbr_name        
    ,is_vip          
    ,sex             
    ,birthday        
    ,vip_level       
    ,page_chnl_level1_id 
    ,page_chnl_level1_name 
    ,page_chnl_level2_id 
    ,page_chnl_level2_name 
    ,long_user_id    
    ,spm_id          
    ,scm_id          
    ,logkey          
    ,pid             
    ,str_to_map(args, ',', '=') args
	,ds
	,site
	,case when spm_id in ( 'a2h0c.8166619.history.clear'
                         ,'a2h0c.8166619.page.back'
                         ,'a2h0c.8166622.feedback.suggest'
                         ,'a2h0c.8166622.filter.sfilter'
                         ,'a2h0c.8167934.page.back'
                         ,'a2h0c.8167945.page.back'
                         ,'a2h0c.8167947.page.back'
                         ,'a2h0c.8167948.page.back'
                         ,'a2h0c.8214523.page.back'
                         ,'a2h0c.8166619.searcharea.cancelbutton'
                         ,'a2h0c.8166619.searcharea.clearbutton'
                         ,'a2h0c.8166622.filter.channeltab'
                         ,'a2h0c.8166622.noresult.suggest'
                         ,'a2h0c.8166622.page.back'
                         ,'a2h0c.8166622.page.morerefresh'
                         ,'a2h0c.8166622.searcharea.activesearch'
                         ,'a2h0c.8166622.searcharea.cancelbutton'
                         ,'a2h0c.8167934.searchtop.title'
                         ,'a2h0c.8167947.filter.seq'
                         ,'a2h0c.8167948.filter.catetab'
                         ,'a2h0c.8214523.detail.expander') then '0'
         when spm_id in ('a2h0c.8166619.hotkeyword.search'
                          ,'a2h0c.8166619.history.search'
                          ,'a2h0c.8166619.kubox.search'
                          ,'a2h0c.8166619.searcharea.keyinput'
                          ,'a2h0c.8166619.searcharea.searchbutton'
                          ,'a2h0c.8166622.searcharea.searchbutton'
                          ,'a2h0c.8167934.searchtop.search'
						              ,'a2h0c.8166619.hint.1'
                          ,'a2h0c.8166619.hot.1'
                          ,'a2h0c.8166619.history.1') then '1'
    else '3' end logtype
from 
    ytcdm.dwd_yt_log_wl_app_clk_di a 
where 
    ds = '${ds}' and 
	site = 'youku' and  -- 只取youku的数据
	((app_ver >= '5.10.3' and dev_type='phone')  or (app_ver >= '4.9' and dev_type='pad') )  
	and coalesce(split(spm_id, '\\.')[0]) = 'a2h0c' -- 搜索的spm.a标识
;

-- select * from ytsoku.dwd_soku_app_query_click_utsdk_log_di limit 100;