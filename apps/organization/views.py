# -*-coding:utf-8-*-
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from .models import CourseOrg, CityDict
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .forms import UserAskForm

from django.http import HttpResponse


class OrgListView(View):
    """
    机构列表
    """

    def get(self, request):
        all_citys = CityDict.objects.all()
        all_orgs = CourseOrg.objects.all()
        # 　热门机构排序
        hot_orgs = CourseOrg.objects.all().order_by('click_num')[:3]

        # 搜索
        # search_keywords = request.GET.get('keywords', '')
        # if search_keywords:
        #     all_orgs = all_orgs.filter(Q(name__icontains=search_keywords) |
        #                                Q(desc__icontains=search_keywords)
        #                                )

        # 选择机构类别
        category = request.GET.get('cate', '')
        if category:
            all_orgs = all_orgs.filter(category=category)

        # 选择城市
        city_id = request.GET.get('city', '')
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))

        # 排序
        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'students':
                all_orgs = all_orgs.order_by('-students')
            elif sort == 'course_nums':
                all_orgs = all_orgs.order_by('-course_nums')

        numbers = all_orgs.count()
        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_orgs, 5, request=request)
        orgs = p.page(page)

        return render(request, 'org-list.html', {
            'all_citys': all_citys,
            'all_orgs': orgs,
            'numbers': numbers,
            'sort': sort,
            'category': category,
            'city_id': city_id,
            'hot_orgs': hot_orgs,
        })


class AddUserAsk(View):
    """
    用户咨询
    """

    def post(self, request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            user_ask = userask_form.save(commit=True)

            return HttpResponse("{'status:'success'}", content_type='application/json')
        else:
            return HttpResponse("{'status:'fail','msg':{}}".format(userask_form.errors))
