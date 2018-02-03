# -*- coding: utf8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .models import Course, CourseResource
from operation.models import UserFavorite, CourseComments
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


class CourseListView(View):
    """

    """
    def get(self, request):
        """
        课程列表
        """
        sort = request.GET.get('sort', '')
        all_courses = Course.objects.all().order_by('-add_time')
        hot_courses = Course.objects.all().order_by('-click_nums')[:3]
        if sort:
            if sort == 'hot':
                all_courses = all_courses.order_by("-click_nums")
            elif sort == 'students':
                all_courses = all_courses.order_by("-students")

        # 对课程机构列表进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_courses, 20, request=request)

        courses = p.page(page)
        return render(request, 'course-list.html', {
            'sort': sort,
            'all_courses': courses,
            'hot_courses': hot_courses,
        })


class CourseDetailView(View):
    """
    课程详情页
    """
    def get(self, request, course_id):
        course = Course.objects.get(id=course_id)
        # 增加课程点击数
        course.click_nums += 1
        course.save()

        has_fav_course = False
        has_fav_org = False

        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
                has_fav_course = True
            if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=2):
                has_fav_org = True

        # 根据tag查询推荐课程
        tag = course.tag
        if tag:
            relate_courses = Course.objects.filter(tag=tag).exclude(id=course_id).order_by('?')[:2]
        else:
            relate_courses = []
        return render(request, 'course-detail.html', {
            'course': course,
            'relate_courses': relate_courses,
            'has_fav_course': has_fav_course,
            'has_fav_org': has_fav_org,
        })


class CourseInfoView(View):
    """
    课程详情内页，主要是课程章节和资源下载的相关信息
    """
    def get(self, request, course_id):
        course = Course.objects.get(id=course_id)
        course_resources = CourseResource.objects.filter(course=course)
        return render(request, 'course-video.html', {
            'course': course,
            'course_resources': course_resources,
        })


class CourseCommentsView(View):
    """
    用户评论页面
    """
    def get(self, request, course_id):
        course = Course.objects.get(id=course_id)
        all_comments = CourseComments.objects.filter(course=course.id).order_by('-add_time')
        course_resources = CourseResource.objects.filter(course=course)

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_comments, 5, request=request)

        all_comments = p.page(page)
        return render(request, 'course-comment.html', {
            'course': course,
            'all_comments': all_comments,
            'course_resources': course_resources,
        })


class AddCommentView(View):
    def post(self, request):
        # 验证用户登录态
        if not request.user.is_authenticated():
            return HttpResponse('{"status": "fail", "msg": "用户未登录"}', content_type='application/json')

        course_id = int(request.POST.get('course_id', 0))
        comment = request.POST.get('comments', '')
        if course_id > 0 and comment:
            user_comment = CourseComments()
            course = Course.objects.get(id=course_id)
            user_comment.user = request.user
            user_comment.course = course
            user_comment.comments = comment
            user_comment.save()
            return HttpResponse('{"status": "success", "msg": "评论成功"}', content_type='application/json')
        else:
            return HttpResponse('{"status": "fail", "msg": "评论出错"}', content_type='application/json')

