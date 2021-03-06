from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', 'qa.views.test'),
    #url(r'^login/.*$', 'qa.views.test'),
    #url(r'^signup/.*$', 'qa.views.test'),
    #url(r'^popular/.*$', 'qa.views.test'),
    #url(r'^ask/.*$', 'qa.views.test'),
    #url(r'^new/.*$', 'qa.views.test'),
    #url(r'^question/(?P<id>\d+)/$', 'qa.views.test'),
    #url(r'^$', 'qa.views.test'),
    url(r'^$', 'qa.views.main_view'),
    url(r'^popular/.*$', 'qa.views.popular_view'),
    url(r'^question/(?P<q_id>\d+)/$', 'qa.views.question_view', name='question'),
    url(r'^ask/$', 'qa.views.question_add'),    
    url(r'^answer/$', 'qa.views.answer_add'),
    url(r'^signup/.*$', 'qa.views.signup_view'),
    url(r'^login/.*$', 'qa.views.login_view'),
    url(r'^logout/.*$', 'qa.views.logout_view'),

)
