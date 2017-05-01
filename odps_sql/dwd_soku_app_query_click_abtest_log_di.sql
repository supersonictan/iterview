--odps sql 
--********************************************************************--
--@ author:恩驰
--@ create time:2017-03-14 14:34:51
--@ 上线管理: **每次上线需做变更说明, 管理员才能发布**
--@ v1.0: 变更说明 | 变更时间
--********************************************************************--

-- 搜索结果页点击视频，节目，播单控件；
-- 对于节目点击poster title playbutton 传节目id 其他情况均传视频id
use ytsoku;
CREATE TABLE IF NOT EXISTS dwd_soku_app_query_click_abtest_log_di
(
    expid_abd             STRING             COMMENT '实验号abd位',
    expid                 STRING             COMMENT '实验号',	
	object_id             STRING             COMMENT '点击的object_id',
    object_type           STRING             COMMENT '1:视频 2:节目',
	show_code             STRING             COMMENT '归一节目show_code',
    ip                    STRING             COMMENT 'IP：格式为如 192.169.1.1',
    guid                  STRING             COMMENT 'GUID：GUID',
    utdid                 STRING             COMMENT 'UTDID：utdid',
    server_time           STRING             COMMENT '服务器收集时间：服务器收集时间',
    local_time            STRING             COMMENT '客户端采集时间：客户端采集时间',
    se_id                 STRING             COMMENT '会话ID：会话ID',
    clk_object_id         STRING             COMMENT '控件ID：对应原refercode.内容id',
    clk_object_name       STRING             COMMENT '控件名称：控件名称',
    pre_clk_object_name   STRING             COMMENT '上一个控件名称(此字段暂时没有意义，请勿使用)',
    clk_object_num        STRING             COMMENT '控件序号：对应原refercode.内容序号',
    clk_object_type       STRING             COMMENT '控件内容类型：控件内容类型，对应原refercode.内容类型，和object_id配合使用',
    clk_object_title      STRING             COMMENT '控件内容标题：如;papi酱逛家居店泣血体验',
    page                  STRING             COMMENT '页面名称：页面名称',
    ut_event_id           BIGINT             COMMENT 'UT事件ID：UT事件ID：2001 页面浏览 详见http://tbdocs.alibaba-inc.com/pages/viewpage.action?pageId=199471773',
    network               STRING             COMMENT '网络类型：wifi;2G;3G;4G',
    mac                   STRING             COMMENT 'MAC地址：终端的MAC地址',
    imei                  STRING             COMMENT '移动设备国际身份码缩写：移动设备国际身份码缩写',
    idfa                  STRING             COMMENT '广告标示符：广告标示符（IDFA-identifierForIdentifier）',
    os_name               STRING             COMMENT '操作系统名称：操作系统名称如android,ios 等',
    os_ver                STRING             COMMENT '操作系统版本：4.1;9.2',
    app_key               STRING             COMMENT 'APPKEY：APPID 中@前面的数字',
    app_ver               STRING             COMMENT '客户端版本：youku android:5.7.1; youku iphone:5.8',
    sdk_ver               STRING             COMMENT 'SDK版本：APP SDK的版本',
    resolution            STRING             COMMENT '分辩率：终端的分辨率,如1024X768',
    dev_type              STRING             COMMENT '终端类型：phone/pad/tv/pc',
    dev_brand             STRING             COMMENT '终端品牌：苹果;三星;小米',
    model_type            STRING             COMMENT '机型：细分的机型，如P7，iphone5s',
    carrier               STRING             COMMENT '电信运营商：电信运营商 carrier, 中国联通，中国移动，中国电信',
    country_name          STRING             COMMENT '国家中文名称：国家中文名称：如中国、美国',
    province_name         STRING             COMMENT '省份中文名称：省份中文名称：如北京、上海',
    city_name             STRING             COMMENT '城市中文名称：城市中文名称：如 杭州、长沙',
    mbr_id                BIGINT             COMMENT '会员ID：会员ID',
    mbr_name              STRING             COMMENT '会员名称：会员名称',
    is_vip                STRING             COMMENT '是否VIP会员：Y：是 N:否',
    sex                   STRING             COMMENT '性别：0=女,1=男,2=保密',
    birthday              STRING             COMMENT '生日：生日',
    vip_level             BIGINT             COMMENT '会员级别：黄金、白银、其他',
    page_chnl_level1_id   BIGINT             COMMENT '一级页面频道ID：一级页面频道ID',
    page_chnl_level1_name STRING             COMMENT '一级页面频道名称：一级页面频道名称',
    page_chnl_level2_id   STRING             COMMENT '二级页面频道ID：二级页面频道ID',
    page_chnl_level2_name STRING             COMMENT '二级页面频道名称：二级页面频道名称',
    long_user_id          STRING             COMMENT '长登录用户ID：长登录用户ID',
    spm_id                STRING             COMMENT '控件SPM：点击位置的abcd位',
    scm_id                STRING             COMMENT 'SCMID：SCM标识符',
    logkey                STRING             COMMENT '日志请求串：如pv日志的/1.gif,黄金令箭日志的定位串 /sns.1.1,*.gif说明见：http://baike.corp.taobao.com/index.php/AliLog',
    pid                   STRING             COMMENT '渠道ID：在每个应用商店中APP会有一个标识符，能够在应用商店中唯一标识这个APP以及APP适用的终端',
    args                  MAP<STRING,STRING> COMMENT '',
	spm_a                 STRING             COMMENT '',
	spm_b                 STRING             COMMENT '',
	spm_c                 STRING             COMMENT '', 
	spm_d                 STRING             COMMENT '', 
	is_ogc                STRING             COMMENT '1为ogc, 其他为0',
	ogc_type              STRING             COMMENT ''
)
COMMENT '搜库APP搜索与点击表-ABTEST'
PARTITIONED BY 
(
    ds                    STRING             COMMENT '分区字段：账期，YYYYMMDD', 
	device_flag           STRING             COMMENT '终端标识'
)
LIFECYCLE 365;


insert overwrite table dwd_soku_app_query_click_abtest_log_di partition (ds, device_flag)
select 
	 concat(split(expid, '\\.')[0], '.', split(expid, '\\.')[1], '.',  split(expid, '\\.')[3]) expid_abd
	,expid
	,a.object_id  
	,if(length(a.object_id) < 19, '1', '2') object_type
	,show_code
    ,ip                    
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
    ,args      
	,spm_a
	,spm_b 
	,spm_c 
	,spm_d 
	,is_ogc
	,ogc_type
	,ds
	,device_flag
from 
    (select 
        a.*,
        if(b.object_id is not null, 1, 0) is_ogc,
		b.show_code,
		b.type ogc_type
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
    		lower(trim(split(a.spm_id,"\\.")[3])) spm_d,
            args['object_id'] object_id
    	from 
    		ytsoku.dwd_soku_app_query_click_utsdk_log_di a 
    	where 
    		ds = '${ds}' 
    		--and lower(trim(split(a.spm_id,"\\.")[1])) = '8166622'  -- 搜索结果页
    		and clk_object_type in ('1', '2', '3')  -- 必须是点击视频:1，节目:2或者播单:3
			and lower(trim(split(a.spm_id,"\\.")[3])) in ('poster', 'title', 'screenshot', 'playbutton', 'selectbutton', 'selectlist')
			and args['object_id'] is not null 
            and length(args['object_id']) >= 5 
            and length(args['object_id']) < 25  --符合节目id 视频id规则
    	) a 
    left outer join 
        (select 
            vdo_code object_id,
            vdo_id   object_id_inner,
        	show_code,
        	show_id,
    		'1' type
        from 
            ytcdm.dim_yt_vdo
        where 
            ds = '${ds}' 
            and site = 'youku' 
            and copyright = 'authorized' and show_id is not null
        union all 
        select 
            show_code object_id,
            cast(show_id as string)   object_id_inner,
        	show_code,
        	show_id,
    		'2' type
        from 
            ytcdm.dim_yt_show
        where 
            ds = '${ds}' and site = 'youku' and 
        	copyright = 'authorized' and show_id is not null
        ) b 
	on a.object_id = b.object_id
	) a 
; 


-- a2h0c.8166622.r<log_cate>.poster
-- a2h0c.8166622.r<log_cate>.title
-- a2h0c.8166622.r<log_cate>.screenshot
-- a2h0c.8166622.r<log_cate>.playbutton
-- a2h0c.8166622.r<log_cate>.selectbutton
-- use ytsoku;
-- select spm_d, length(object_id) lllen, count(*) rm 
-- from ytsoku.dwd_soku_app_query_click_abtest_log_di
-- where ds = '20170314'
-- group by spm_d, length(object_id) 
-- order by rm desc;
-- 
-- use ytsoku;
-- select * from ytsoku.dwd_soku_app_query_click_abtest_log_di where ds = '20170314' limit 20;