from django.conf.urls import url

from home import views

app_name = 'home'

urlpatterns = [
    url(r'^$', views.home.as_view(), name='home'),
    url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.Create, name='create')

]
