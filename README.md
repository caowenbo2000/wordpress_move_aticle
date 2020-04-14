# wordpress_move_aticle
一个博客搬家脚本，用于把csdn博客迁移到wordpress上，也可从别处搬家，自行修改链接
# 环境
python3  
一系列prthon库
# 过程
抓取我csdn上的博客主页页面中所有的文章链接  
对链接访问 抓出  title date 和博客content  
然后使用wordpress的api直接post
