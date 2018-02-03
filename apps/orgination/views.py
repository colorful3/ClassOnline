# -*- coding: utf8 -*-
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import View
from .models import CourseOrg, CityDict
from courses.models import Course
from django.shortcuts import render_to_response
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .forms import UserAskForm
from operation.models import UserFavorite

# Create your views here.


# url http://127.0.0.1:8000/org/list
class OrgView(View):
    def get(self, request):
        # 根据点击数的
        # 所有的课程机构
        all_orgs = CourseOrg.objects.all()
        # 所有的城市
        all_citys = CityDict.objects.all()
        # 页面右侧授课机构排名
        hot_orgs = all_orgs.order_by("-click_nums")[:3]
        # 取出所选的city id
        city_id  = request.GET.get('city', "")
        # 列别筛选
        category = request.GET.get('ct', "")
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))

        if category:
            all_orgs = all_orgs.filter(category=category)

        # 学习人数筛选
        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'students':
                all_orgs = all_orgs.order_by("-students")
            elif sort == 'courses':
                all_orgs = all_orgs.order_by("-course_nums")
        # 数量
        org_nums = all_orgs.count()

        # 对课程机构列表进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_orgs, 5, request=request)

        orgs = p.page(page)

        return render(request, 'org-list.html', {
            'all_orgs': orgs,
            'all_citys': all_citys,
            'org_nums': org_nums,
            'city_id': city_id,
            'category': category,
            'hot_orgs': hot_orgs,
            'sort': sort,
        })


class AddUserAskView(View):
    def post(self, request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            user_ask = userask_form.save(commit=True)
            return HttpResponse('{"status": "success"}', content_type='application/json')
        else:
            return HttpResponse('{"status": "fail", "msg": "添加错误"}', content_type='application/json')


class OrgHomeView(View):
    """
    机构首页
    """
    def get(self, request, org_id):
        current_page = 'home'
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        all_courses = course_org.course_set.order_by('?').all()[:3]  # 得到课程的信息。
        all_teachers = course_org.teacher_set.all().order_by('?')[:1] # 得到机构教师的信息
        return render(request, 'org-detail-homepage.html', {
            'all_courses': all_courses,
            'all_teachers': all_teachers,
            'course_org': course_org,
            'current_page': current_page,
            'has_fav': has_fav
        })


class OrgCourseView(View):
    """
    机构课程
    """
    def get(self, request, org_id):
        current_page = 'course'
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        course_org = CourseOrg.objects.get(id=int(org_id))
        all_courses = course_org.course_set.order_by('?').all()
        return render(request, 'org-detail-course.html', {
            'all_courses': all_courses,
            'course_org': course_org,
            'current_page': current_page,
            'has_fav': has_fav
        })


class OrgDescView(View):
    """
    机构描述
    """
    def get(self, request, org_id):
        current_page = 'desc'
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        course_org = CourseOrg.objects.get(id=int(org_id))
        return render(request, 'org-detail-desc.html', {
            'current_page': current_page,
            'course_org':course_org,
            'has_fav': has_fav
        })


class OrgTeacherView(View):
    """
    机构讲师
    """
    def get(self, request, org_id):
        current_page = 'teacher'
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        all_teachers = course_org.teacher_set.all().order_by('?') # 得到机构教师的信息
        return render(request, 'org-detail-teachers.html', {
            'current_page': current_page,
            'course_org':course_org,
            'all_teachers': all_teachers,
            'has_fav': has_fav
        })


class AddFavView(View):
    """
    用户收藏\取消收藏
    """
    def post(self, request):
        fav_id = int(request.POST.get('fav_id', 0))
        fav_type = int(request.POST.get('fav_type', 0))

        # 判断用户是否登录状态
        if not request.user.is_authenticated():
            return HttpResponse('{"status": "fail", "msg": "用户未登录"}', content_type='application/json')
        exist_records = UserFavorite.objects.filter(user=request.user, fav_id=fav_id, fav_type=fav_type)
        if exist_records:
            # 如果记录已经存在，则表示用户取消收藏
            exist_records.delete()
            return HttpResponse('{"status": "success", "msg": "收藏"}', content_type='application/json')
        else:
            # 添加收藏
            user_fav = UserFavorite()
            if fav_id > 0 and fav_type > 0:
                user_fav.user = request.user
                user_fav.fav_id = fav_id
                user_fav.fav_type = fav_type
                user_fav.save()
                return HttpResponse('{"status": "success", "msg": "已收藏"}', content_type='application/json')
            else:
                return HttpResponse('{"status": "fail", "msg": "收藏出错"}', content_type='application/json')
