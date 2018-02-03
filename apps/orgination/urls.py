# -*- coding: utf8 -*-
__author__ = 'Colorful'
__date__ = '2018/1/28 下午6:18'

from django.conf.urls import url
from .views import OrgView, AddUserAskView, OrgHomeView, OrgCourseView, OrgDescView, OrgTeacherView, AddFavView

urlpatterns = [
    # 课程机构列表首页
    url(r'^list/$', OrgView.as_view(), name='org_list'),
    url(r'^add_ask/$', AddUserAskView.as_view(), name='add_ask'),
    url(r'^home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name='org_home'),
    url(r'^course/(?P<org_id>\d+)/$', OrgCourseView.as_view(), name='org_course'),
    url(r'^desc/(?P<org_id>\d+)/$', OrgDescView.as_view(), name='org_desc'),
    url(r'^teachers/(?P<org_id>\d+)/$', OrgTeacherView.as_view(), name='org_teachers'),

    # 用户收藏
    url(r'^add_fav/$', AddFavView.as_view(), name='add_fav')
]