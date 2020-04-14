# coding:utf-8
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.methods import posts
from wordpress_xmlrpc.methods import taxonomies
from wordpress_xmlrpc import WordPressTerm
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts
import sys
from datetime import datetime
# reload(sys)
# sys.setdefaultencoding('utf-8')
def Ssubmit(Tittle, Content,Time):
    wp = Client('http://caowenbo.top/xmlrpc.php', 'admin', 'password')

    post = WordPressPost()
    post.title = Tittle
    post.content = Content
    post.post_status = 'publish'  # 文章状态，不写默认是草稿，private表示私密的，draft表示草稿，publish表示发布
    post.date = datetime.strptime(Time, '%Y-%m-%d') # 发布时间
    post.terms_names = {
        #'post_tag': ['test', 'firstpost'],  # 文章所属标签，没有则自动创建
        'category': ['解题报告']  # 文章所属分类，没有则自动创建
    }
    post.id = wp.call(posts.NewPost(post))
#Ssubmit('asd','asd','2000-1-1')