from django.conf.urls import patterns, include, url
from django.contrib import admin
import singleblog.views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blogs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', singleblog.views.index, name='index'),
   
    url(r'^archive/', singleblog.views.archive, name="archive"), 
    url(r'^article/(?P<id>(\d+))$', singleblog.views.view_blog, name='blog_article'),
    url(r'^author/(?P<id>(\d+))$', singleblog.views.view_author, name='blog_author'),
    url(r'^author/(?P<url>(\S+))$', singleblog.views.view_url, name='author_url'), 
    url(r'^category/(?P<cid>(\d+))$', singleblog.views.category, name='category'),
    url(r'^tag/(?P<tid>(\d+))$', singleblog.views.tag, name='tag'),
    
    #user register and login
    url(r'^login/$', singleblog.views.login, name='login'),
    url(r'^register/$', singleblog.views.register, name='register'),
    url(r'^logout/$', singleblog.views.logout, name='logout'),

    #
    url(r'^search/', singleblog.views.search, name='search'),
    
    #
    url(r'user/blog/add/$', singleblog.views.add_blog, name='add_blog'),
    url(r'^user/blog/edit/(?P<id>(\d+))/$', singleblog.views.edit_blog, name='edit_blog'),
    url(r'^user/blog/remove/(?P<id>(\d+))/$', singleblog.views.remove_blog, name='remove_blog'),

    #
    url(r'user/comment/add/(?P<id>(\d+))/$', singleblog.views.add_comment, name='add_comment'),
    #url(r'user/comment/reply/(?P<id>(\d+))/$', singleblog.views.reply_comment, name='reply_comment'),
    url(r'user/comment/remove/(?P<id>(\d+))/$', singleblog.views.remove_comment, name='remove_comment'),
    url(r'user/comment/read/(?P<id>(\d+))/$', singleblog.views.read_comment, name="read_comment"),

    url(r'^user/letter/send/$', singleblog.views.send_letter, name="send_letter"),
    url(r'^user/letter/read/(?P<id>(\d+))/$', singleblog.views.read_letter, name="read_letter"),
    url(r'^user/message/view/', singleblog.views.view_history_message, name="view_history"),
    url(r'^user/message/delete/', singleblog.views.delete_messages, name="delete_messages"),

    #some ajax url for ajax
    url(r'^user/password/reset/', singleblog.views.reset_password, name="reset_password"),
    url(r'^user/password/forget/$', singleblog.views.forget_password, name="forget_password"),
    url(r'^user/avatar/reset/$', singleblog.views.set_avatar, name="set_avatar"),
    url(r'^ajax_set_author_info/$', singleblog.views.ajax_set_author_info, name='ajax_set_author_info'),
    url(r'^user/category/edit/$', singleblog.views.edit_category, name='edit_category'),
    url(r'^user/tag/edit/$', singleblog.views.edit_tag, name='edit_tag'),
	
    url(r'^getverifycode/', singleblog.views.get_verifycode, name='get_verifycode'),
    url(r'^upload/images/$', singleblog.views.upload_images, name='upload_images'),
    url(r'^about/$', singleblog.views.about, name="about"),
    url(r'^contact/$', singleblog.views.contact, name="contact"),
    url(r'^leave_message/$', singleblog.views.leave_message, name="leave_message"),
)




    

        

