# -*- coding: utf8 -*-
__author__ = 'Colorful'
__date__ = '2018/1/23 下午11:00'
from .models import CityDict, CourseOrg, Teacher

import xadmin


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'address', 'add_time']
    search_fields = ['name', 'desc', 'address']
    list_filter = ['name', 'desc', 'address', 'add_time']


class TeacherAdmin(object):
    list_display = ['name', 'work_years', 'work_company','work_position', 'add_time']
    search_fields = ['org', 'name', 'work_years', 'work_position']
    list_filter = ['org__name', 'name', 'work_years', 'work_company', 'add_time']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)