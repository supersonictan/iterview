#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

s = """    </tr>
      <tr>
      <td colspan="2" align="center" valign="top"><div align="left"><div

style="float:right; margin:5px;"><script language=javascript src="/js1/120.js"></script></div><div id="Zoom">
<!--Content Start--><span style="FONT-SIZE: 12px"><td>
<p>西游伏妖篇][HD-mkv.720p.国语中字][2017年动作喜剧]<br /><br /><img onclick="if(this.width&gt;screen.width-461) window.open('http://image18.poco.cn/mypoco/myphoto/20170418/14/185036732201704181430092710385600361_004.jpg');" border="0" src="http://image18.poco.cn/mypoco/myphoto/20170418/14/185036732201704181430092710385600361_004.jpg" alt="" /><br /><br />◎片　　名　西游伏妖篇/西游2：伏妖篇/西游降魔篇2/西游&middot;降魔篇2/西游&middot;降魔2<br />◎又　　名　Journey to the West: The Demons Strike Back/Journey to the West: Demon Chapter<br />◎年　　代　2017<br />◎地　　区　中国/中国香港<br />◎类　　型　喜剧/动作/奇幻/古装<br />◎语　　言　普通话<br />◎字　　幕　中文<br />◎IMDb评分&nbsp; 5.7/10 from 742 users<br />◎文件格式　RMVB + AAC<br />◎视频尺寸　1280 x 720<br />◎文件大小　1CD<br />◎片　　长　108分钟<br />◎导　　演　徐克&nbsp; Hark Tsui<br />◎主　　演　吴亦凡&nbsp; Kris Wu<br />　　　　　　林更新&nbsp; Gengxin Lin<br />　　　　　　姚晨&nbsp; Chen Yao<br />　　　　　　林允&nbsp; Yun Lin<br />　　　　　　包贝尔&nbsp; Bei&lsquo;er Bao<br />　　　　　　巴特尔&nbsp; Mengke Bateer<br />　　　　　　杨一威&nbsp; Yiwei Yang<br />　　　　　　大鹏&nbsp; Da Peng<br />　　　　　　王丽坤&nbsp; Likun Wang<br />　　　　　　汪铎&nbsp; Duo Wang<br />　　　　　　张美娥&nbsp; Mei&lsquo;e Zhang<br /><br />◎简　　介<br /><br />　　历经千辛万苦，唐僧（吴亦凡 饰）、孙悟空（林更新 饰）、猪八戒（杨一威 饰）、沙僧（巴特尔 饰）这支取经团队朝着最终的目标持续前进，然而这一过程中他们不仅忍饥挨饿，还矛盾频生，似乎随时都有分裂的危险。尤其法师念念不忘死去的段小姐（舒淇 饰），而这件事也成为他和悟空之间矛盾和争吵的根源。在摆脱了蜘蛛精的纠缠后，师徒四人来至充满童趣的比丘国。比丘国王（包贝尔 饰）精神错乱，如同孩子般喜怒无常。国师九宫真人（姚晨 饰）将师徒迎进王宫，虽百般叮咛，却仍引出不少的乱子，甚至还揪出了藏在宫中的狡猾妖怪。<br />&nbsp; <br />　　冒险仍在继续，师徒间的危机一触即发&hellip;&hellip;<br /><br /><img onclick="if(this.width&gt;screen.width-461) window.open('http://image18.poco.cn/mypoco/myphoto/20170418/14/185036732201704181430092710385600361_002.jpg');" border="0" src="http://image18.poco.cn/mypoco/myphoto/20170418/14/185036732201704181430092710385600361_002.jpg" alt="" /></p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p><strong><font color="#ff0000" size="4">【下载地址】</font></strong></p>
<p>&nbsp;</p>
<p>
<table style="BORDER-BOTTOM: #cccccc 1px dotted; BORDER-LEFT: #cccccc 1px dotted; TABLE-LAYOUT: fixed; BORDER-TOP: #cccccc 1px dotted; BORDER-RIGHT: #cccccc 1px dotted" border="0" cellspacing="0" cellpadding="6" width="95%" align="center">
    <tbody>
        <tr>
            <td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="ftp://ygdy8:ygdy8@y153.dydytt.net:8261/[阳光电影www.ygdy8.com].西游伏妖篇.HD.720p.国语中字.mkv">ftp://ygdy8:ygdy8@y153.dydytt.net:8261/[阳光电影www.ygdy8.com].西游伏妖篇.HD.720p.国语中字.mkv</a></td>
        </tr>
"""

matcher = re.findall('src="http:.*?jpg',s)
print matcher
