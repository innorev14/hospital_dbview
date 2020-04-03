from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .models import *

class KeywordView(ListView):
    model = DeptAndKeyword
    template_name = 'hospital/keyword_list.html'

def keywordview(request):
    if request.method == "GET":
        req_keyword = request.GET.get('q', '')
        dept = Department.objects.all()

        req_dept = request.GET.get('dept', '')
        dept_keyword = DeptAndKeyword.objects.filter(Q(dept_id=req_dept)).order_by('name')

        req_depth1 = request.GET.get('depth1', '')
        depth_one = DepthOneKeyword.objects.all()
        depth1_rel = DepthOneRel.objects.filter(Q(keyword=req_depth1)).order_by('relkeyword')
        req_depth2 = request.GET.get('depth2', '')
        depth_two = DepthTwoKeyword.objects.all()
        depth2_rel= DepthTwoRel.objects.filter(Q(keyword=req_depth2)).order_by('relkeyword')
        req_depth3 = request.GET.get('depth3', '')
        depth_three = DepthThreeKeyword.objects.all()
        depth3_rel= DepthThreeRel.objects.filter(Q(keyword=req_depth3)).order_by('relkeyword')


        rel_keyword = JamesMainKeywordRel.objects.filter(Q(main_keyword=req_keyword))
        naverapi = JamesKeywordNaverapi.objects.filter(Q(keyword=req_keyword))

        context = {
            'dept': dept,
            'dept_keyword': dept_keyword,
            'rel_keyword': rel_keyword,
            'naverapi': naverapi,
            'depth_one': depth_one,
            'depth1_rel': depth1_rel,
            'depth_two': depth_two,
            'depth2_rel': depth2_rel,
            'depth_three': depth_three,
            'depth3_rel': depth3_rel,
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
