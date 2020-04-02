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
        dept = Department.objects.using('read1').filter(Q(dept=req_keyword))
        dept_keyword = DeptAndKeyword.objects.using('read1').filter(Q(dept_id=req_keyword)).select_related().order_by('name')
        rel_keyword = JamesMainKeywordRel.objects.using('read1').filter(Q(main_keyword=req_keyword))
        naverapi = JamesKeywordNaverapi.objects.using('read2').filter(Q(keyword=req_keyword))

        context = {
            'dept': dept,
            'dept_keyword': dept_keyword,
            'rel_keyword': rel_keyword,
            'naverapi': naverapi,
        }
        return render(request, template_name='hospital/department_list.html', context=context)

    if request.method == 'POST':
        req_keyword = request.GET.get('q', '')
        print(req_keyword)
        dept = Department.objects.using('read1').values()
        dept_keyword = DeptAndKeyword.objects.using('read1').select_related().order_by('name')

        rel_keyword = JamesMainKeywordRel.objects.using('read1').values()
        naverapi = JamesKeywordNaverapi.objects.using('read2').values()

        if req_keyword in dept_keyword.select_related('dept_id'):
            context = {
                'dept': dept,
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
    naverapi = JamesKeywordNaverapi.objects.using('read2').values()
    context = {
        'naverapi': naverapi,
    }
    return render(request, 'hospital/naverapi_list.html', context=context)
