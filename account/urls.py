from django.conf.urls import url
from django.contrib.auth.views import login,logout,password_reset,password_reset_done,password_reset_confirm,password_reset_complete

from account import views
app_name = 'account'

urlpatterns = [


    url(r'^login/', login, {'template_name': 'account/login.html'}, name='login'),
    url(r'^logout/', logout, {'template_name': 'account/logout.html'}, name='logout'),

    url(r'^register/', views.register , name='register'),

    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/(?P<pk>\d+)/$', views.profile, name='profilepk'),
    url(r'^profile/edit/$', views.edit_profile, name='editprofile'),
    url(r'^changepass/$', views.changepass, name='changepass'),

    url(r'^passwordreset/$',password_reset,
        {'template_name':'account/reset.html', 'post_reset_redirect': 'account:password_reset_done'
         , 'email_template_name':'account/reset_email.html'},
        name='passwodreset'),

    url(r'^passwordreset/done/$', password_reset_done, {'template_name': 'account/pass_reset_done.html'}, name= "password_reset_done" ),

    url(r'^passwordreset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
        {'post_reset_redirect': 'account:password_reset_confirm','template_name':'account/reset_confirm.html'},
        name="password_reset_confirm"),


    url(r'^passwordreset/complete/$', password_reset_complete,  {'template_name': 'account/pass_complete.html'},name="password_reset_complete"),

]
