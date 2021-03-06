from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .models import *

class KeywordView(ListView):
    model = DeptAndKeyword
    template_name = 'hospital/keyword_list.html'
    paginate_by = 100

    def get_queryset(self, *args, **kwargs):
        qs = JamesKeywordNaverapi.objects.all().order_by('-mobileclick')
        query = self.request.GET.get("q", None)
        if query is not None:
            q = qs.filter(Q(keyword=query))
        else:
            q = qs
        return q

    def get_context_data(self, *args, **kwargs):
        context = super(KeywordView, self).get_context_data(*args, **kwargs)
        return context


def keywordview(request):
    if request.method == "GET":
        req_keyword = request.GET.get('q', '')
        dept = Department.objects.all()

        req_dept = request.GET.get('dept', '')
        dept_keyword = DeptAndKeyword.objects.filter(Q(dept_id=req_dept)).order_by('name')
        dept_count = DeptAndKeyword.objects.count()

        req_depth1 = request.GET.get('depth1', '')
        depth_one = DepthOneKeyword.objects.all()
        depth1_rel = DepthOneRel.objects.order_by('relkeyword')
        # depth1_rel = DepthOneRel.objects.filter(Q(keyword=req_depth1)).order_by('relkeyword')
        depth1_count = DepthOneRel.objects.count()

        req_depth2 = request.GET.get('depth2', '')
        depth_two = DepthTwoKeyword.objects.all()
        depth2_rel= DepthTwoRel.objects.filter(Q(keyword=req_depth2)).order_by('relkeyword')
        depth2_count = DepthTwoRel.objects.count()

        req_depth3 = request.GET.get('depth3', '')
        depth_three = DepthThreeKeyword.objects.all()
        depth3_rel= DepthThreeRel.objects.filter(Q(keyword=req_depth3)).order_by('relkeyword')
        depth3_count = DepthThreeRel.objects.count()


        rel_keyword = JamesMainKeywordRel.objects.filter(Q(main_keyword=req_keyword))
        naverapi = JamesKeywordNaverapi.objects.filter(Q(relkeyword=req_keyword)).order_by('-mobileclick')
        rel_keyword_count = JamesKeywordNaverapi.objects.count()

        view_device = ViewCountDevice.objects.all()
        view_device_count = ViewCountDevice.objects.all().count()

        view_deviced3 = ViewCountDeviceD3.objects.all()
        view_deviced3_count = ViewCountDeviceD3.objects.all().count()

        view_genderage_count = ViewCountGenderAge.objects.all().count()
        view_genderage = ViewCountGenderAge.objects.all()

        view_genderaged3_count = ViewCountGenderAge.objects.all().count()
        view_genderaged3 = ViewCountGenderAge.objects.all()

        context = {
            'dept': dept,
            'dept_keyword': dept_keyword,
            'dept_count': dept_count,
            'rel_keyword': rel_keyword,
            'naverapi': naverapi,
            'rel_keyword_count': rel_keyword_count,
            'depth_one': depth_one,
            'depth1_rel': depth1_rel,
            'depth1_count': depth1_count,
            'depth_two': depth_two,
            'depth2_rel': depth2_rel,
            'depth2_count': depth2_count,
            'depth_three': depth_three,
            'depth3_rel': depth3_rel,
            'depth3_count': depth3_count,
            'view_device_count': view_device_count,
            'view_device': view_device,
            'view_deviced3_count': view_deviced3_count,
            'view_deviced3': view_deviced3,
            'view_genderage_count': view_genderage_count,
            'view_genderage': view_genderage,
            'view_genderaged3_count': view_genderaged3_count,
            'view_genderaged3': view_genderaged3,
        }
        return render(request, template_name='hospital/department_list.html', context=context)

    if request.method == 'POST':
        req_keyword = request.GET.get('q', '')
        print(req_keyword)
        dept = Department.objects.values()
        dept_keyword = DeptAndKeyword.objects.select_related().order_by('name')

        rel_keyword = JamesMainKeywordRel.objects.values()
        naverapi = JamesKeywordNaverapi.objects.values()

        if req_keyword in dept_keyword.select_related('dept_id'):
            context = {
                'dept': dept,
                'rep_dept': rel_dept,
                'dept_keyword': dept_keyword,
            }
        else:
            pass

        context = {
            'dept': dept,
            'dept_keyword': dept_keyword,
            'rel_keyword': rel_keyword,
            'naverapi': naverapi,
        }
        return render(request, 'hospital/department_list.html', context=context)


def naverAPIListView(request):
    naverapi = JamesKeywordNaverapi.objects.values()
    context = {
        'naverapi': naverapi,
    }
    return render(request, 'hospital/naverapi_list.html', context=context)
