### CSV文件中没有数据
* XPATH在Ipython中尝试过，有数据输出
* 对照上次的模scrapy板，也不知道哪里出错了

### 知道问题但不知道怎么解决
* 从数据分析师首页中爬取招聘详情页时，有些URL=‘javascript:changePage('/JD/web/index/webPosition210!getPostListByConditionShowPic?columnId=2&urlCorpEdition=null&operational=B2176C40F28C0AC9FFF64F7B03443A4EB18D201594CF849D66A225F700A09A7FDB93C7A23D4E7028F1B42493F65BB23EEDDE8835F67F1DD79A1D443B199E3C1ABC438CA65D5FFF09D95C90F66FF09AE4D1036D71FADDA2A89A2CBBD7C2DD4325D71D8F80A378A915F6500E193929FA94',6,10);" 使用正则表达式 m=re.search("javascript:changePage\('(////.+////.+////.+////.+)',[0-9],[0-9];\)",url)，还是出现原来的结果
* 专业要求有些显示在任职资格里，有些没有，不太会用正则表达式处理
* 薪资、福利网站上没有信息
* 查看了整个相关网站信息，招聘岗位的公司只有京东和京东金融，行业、融资情况、公司类型、公司规模根据自己所了解的手动添加
