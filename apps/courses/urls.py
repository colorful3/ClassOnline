# -*- coding: utf8 -*-
__author__ = 'Colorful'
__date__ = '2018/1/30 下午3:36'
from django.conf.urls import url
from .views import CourseListView, CourseDetailView, CourseInfoView, CourseCommentsView, AddCommentView

urlpatterns = [
    # 课程列表页
    url(r'^list/$', CourseListView.as_view(), name='course_list'),
    # 课程详情
    url(r'^detail/(?P<course_id>.*)/$', CourseDetailView.as_view(), name='course_detail'),
    # 课程info
    url(r'^info/(?P<course_id>.*)/$', CourseInfoView.as_view(), name='course_info'),
    # 课程评论展示
    url(r'^comment/(?P<course_id>.*)/$', CourseCommentsView.as_view(), name='course_comment'),
    # 添加课程评论
    url(r'^add_comment/$', AddCommentView.as_view(), name='add_comment')

]
