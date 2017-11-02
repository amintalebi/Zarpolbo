# coding=utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/$', views.register_view, name='register'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^profile/(?P<username>.+)/$', views.profile, name='profile'),
    url(r'^edit_profile/$', views.UserInfoView.as_view(), name='edit_profile')
]