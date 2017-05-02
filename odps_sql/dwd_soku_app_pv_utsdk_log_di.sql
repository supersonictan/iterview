--odps sql 
--********************************************************************--
--@ author:恩驰
--@ create time:2016-11-02 18:24:00
--@ desc: dwd_soku_app_pv_utsdk_log_di
--********************************************************************--

CREATE TABLE IF NOT EXISTS ytsoku.dwd_soku_app_pv_utsdk_log_di
(
    pid                   STRING COMMENT '渠道ID：在每个应用商店中APP会有一个标识符，能够在应用商店中唯一标识这个APP以及APP适用的终端',
    imeisi                STRING COMMENT '设备标识imeisi：设备标识',
    utdid                 STRING COMMENT 'UTDID：utdid',
    guid                  STRING COMMENT 'GUID：GUID，优酷土豆app老式设备唯一标识。',
    idfa                  STRING COMMENT '广告标示符：广告标示符（IDFA-identifierForIdentifier）',
    ip                    STRING COMMENT 'IP：格式为如 192.169.1.1',
    se_id                 STRING COMMENT '会话ID：会话ID',
    server_time           STRING COMMENT '服务器收集时间：服务器收集时间',
    local_time            STRING COMMENT '客户端采集时间：客户端采集时间',
    page                  STRING COMMENT '页面名称：页面名称',
    page_code             STRING COMMENT '当前页面编码：目前为空，UT新采',
    page_type             BIGINT COMMENT '页面类型：1:播放页 2：首页 3：节目页 4：个人页 -99：other',
    page_stay_seconds     BIGINT COMMENT '页面停留时长：页面停留时长',
    vdo_code              STRING COMMENT '视频CODE：视频CODE',
    vdo_id                STRING COMMENT '视频ID：视频ID',
    vdo_title             STRING COMMENT '视频标题：视频标题',
    vdo_len               DOUBLE COMMENT '视频时长：视频时长，单位为分钟',
    vdo_type              STRING COMMENT '视频类型：花絮、资讯、MV、预告片、首映式、正片',
    show_code             STRING COMMENT '节目内部ID加密：节目内部ID加密',
    show_id               BIGINT COMMENT '节目ID：节目ID',
    show_name             STRING COMMENT '节目名称：节目名称',
    owner_id              BIGINT COMMENT '上传者会员ID：上传者会员ID',
    owner_name            STRING COMMENT '上传者会员名称：上传者会员名称',
    vdo_chnl_id           STRING COMMENT '视频频道ID：视频频道ID',
    vdo_chnl_name         STRING COMMENT '频道名称：频道名称',
    page_chnl_level1_id   BIGINT COMMENT '一级页面频道ID：一级页面频道ID',
    page_chnl_level1_name STRING COMMENT '一级页面频道名称：一级页面频道名称',
    country_name          STRING COMMENT '国家中文名称：国家中文名称：如中国、美国',
    province_name         STRING COMMENT '省份中文名称：省份中文名称：如北京、上海',
    city_name             STRING COMMENT '城市中文名称：城市中文名称：如 杭州、长沙',
    mac                   STRING COMMENT 'MAC地址：终端的MAC地址',
    imei                  STRING COMMENT '移动设备国际身份码缩写：移动设备国际身份码缩写',
    app_name              STRING COMMENT 'APPKEY：tudou,youku,laifeng,other',
    app_ver               STRING COMMENT '客户端版本：youku android:5.7.1; youku iphone:5.8',
    dev_type              STRING COMMENT '终端类型：phone/pad',
    model_type            STRING COMMENT '机型：细分的机型，如P7，iphone5s',
    dev_brand             STRING COMMENT '终端品牌：终端品牌 例如： 苹果;三星;小米',
    os_ver                STRING COMMENT '操作系统版本：android4.1;ios9',
    os_name               STRING COMMENT '操作系统名称：操作系统名称如android,ios 等',
    sdk_ver               STRING COMMENT 'SDK版本：UT或者统计SDK的版本',
    long_user_id          STRING COMMENT '长登录用户ID：长登录用户ID',
    network               STRING COMMENT '网络类型：wifi;2G;3G;4G',
    carrier               STRING COMMENT '电信运营商：电信运营商 carrier, 中国联通，中国移动，中国电信',
    resolution            STRING COMMENT '分辩率：终端的分辨率,如1024X768',
    mbr_id                BIGINT COMMENT '会员ID：会员ID',
    mbr_name              STRING COMMENT '会员名称：会员名称',
    is_vip                STRING COMMENT '是否VIP会员：Y：是 N:否',
    vip_level             BIGINT COMMENT '会员级别：黄金、白银、其他',
    sex                   STRING COMMENT '性别：0=女,1=男,2=保密',
    birthday              STRING COMMENT '生日：生日',
    spm_id                STRING COMMENT 'SPMID：超级位置模型，a.b.c.d，a代表站点，b代表当前页面，c代表区块，d为link或按钮',
    url_spm_id            STRING COMMENT '来源SPMID：超级位置模型，a.b.c.d',
    scm_id                STRING COMMENT 'SCMID：SCM标识符',
    url_scm_id            STRING COMMENT '来源SCMID：SCM标识符',
    ut_event_id           BIGINT COMMENT 'UT事件ID：UT事件ID：2001 页面浏览 详见http://tbdocs.alibaba-inc.com/pages/viewpage.action?pageId=199471773',
    args                  MAP<STRING, STRING> COMMENT '扩展字段信息：阿里日志标准扩展字段信息',
    subsc_ids             STRING COMMENT 'SPM所属站点ID串：SPM所属站点ID串',
    url_subsc_ids         STRING COMMENT 'SPM所属站点ID串：SPM所属站点ID串',
    pre_subsc_ids         STRING COMMENT 'SPM所属站点ID串：SPM所属站点ID串',
    spma                  STRING COMMENT 'SPMA：SPM-A位',
    spmb                  STRING COMMENT 'SPMB：SPM-B位',
    url_spma              STRING COMMENT 'SPMA：SPM-A位',
    url_spmb              STRING COMMENT 'SPMB：SPM-B位',
    url_spmc              STRING COMMENT 'SPMC：SPM-C位',
    url_spmd              STRING COMMENT 'SPMD：SPM-D位',
    pre_spma              STRING COMMENT 'SPMA：SPM-A位',
    pre_spmb              STRING COMMENT 'SPMB：SPM-B位',
    pre_spmc              STRING COMMENT 'SPMC：SPM-C位',
    pre_spmd              STRING COMMENT 'SPMD：SPM-D位',
    visitor_id            STRING COMMENT '访问者id：有可能是会员id，有可能是IMEISI,',
    visitor_type          STRING COMMENT '访问者类型：uid：会员 mid:普通访客',
    app_id                STRING COMMENT 'APP_ID：APP的标识符',
    refer_page            STRING COMMENT '来源页面名称',
    refer_args            MAP<STRING, STRING> COMMENT '来源事件参数：事件参数',
    pre_spm_id            STRING COMMENT '来源页的来源SPMID',
    client_code           STRING COMMENT 'APP所属的端：APP所属的端, 如taobao_hd',
    pre_page              STRING COMMENT '来源页的来源PAGE'
)
COMMENT '搜库移动app端pv日志'
PARTITIONED BY (
    ds                    STRING COMMENT '分区字段：账期，YYYYMMDD', 
	site                  STRING COMMENT '分区字段：站点，youku，tudou，laifeng， other')
LIFECYCLE 365;


insert overwrite table ytsoku.dwd_soku_app_pv_utsdk_log_di partition (ds, site)
select 
      pid             
    ,imeisi          
    ,utdid           
    ,guid            
    ,idfa            
    ,ip              
    ,se_id           
    ,server_time     
    ,local_time      
    ,page            
    ,page_code       
    ,page_type       
    ,page_stay_seconds 
    ,vdo_code        
    ,vdo_id          
    ,vdo_title       
    ,vdo_len         
    ,vdo_type        
    ,show_code       
    ,show_id         
    ,show_name       
    ,owner_id        
    ,owner_name      
    ,vdo_chnl_id     
    ,vdo_chnl_name   
    ,page_chnl_level1_id 
    ,page_chnl_level1_name 
    ,country_name    
    ,province_name   
    ,city_name       
    ,mac             
    ,imei            
    ,app_name        
    ,app_ver         
    ,dev_type        
    ,model_type      
    ,dev_brand       
    ,os_ver          
    ,os_name         
    ,sdk_ver         
    ,long_user_id    
    ,network         
    ,carrier         
    ,resolution      
    ,mbr_id          
    ,mbr_name        
    ,is_vip          
    ,vip_level       
    ,sex             
    ,birthday        
    ,spm_id          
    ,url_spm_id      
    ,scm_id          
    ,url_scm_id      
    ,ut_event_id     
    ,str_to_map(args, ',', '=') args            
    ,subsc_ids       
    ,url_subsc_ids   
    ,pre_subsc_ids   
    ,spma            
    ,spmb            
    ,url_spma        
    ,url_spmb        
    ,url_spmc        
    ,url_spmd        
    ,pre_spma        
    ,pre_spmb        
    ,pre_spmc        
    ,pre_spmd        
    ,visitor_id      
    ,visitor_type    
    ,app_id          
    ,refer_page      
    ,str_to_map(refer_args, ',', '=') refer_args      
    ,pre_spm_id      
    ,client_code     
    ,pre_page 
	,ds
	,site
from  
    ytcdm.dwd_yt_log_wl_app_pv_di a 
where 
    ds = '${ds}' and 
	site = 'youku' and  -- 只取youku的数据
	((app_ver >= '5.10.3' and dev_type='phone')  or (app_ver >= '4.9' and dev_type='pad') )   and 
	coalesce(split(spm_id, '\\.')[0]) = 'a2h0c' -- 搜索的spm.a标识
;	