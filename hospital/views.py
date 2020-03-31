from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .models import *


# class KeywordView(ListView):
#     pass

class MyManager(models.Manager):
    def get_queryset(self):
        qs = CustomQuerySet(self.model)
        if self._db is not None:
            qs = qs.using(self._db)
        return qs


def keywordview(request):
    dept = Department.objects.using('read1').values()
    context = {'dept': dept}
    return HttpResponse(request, 'hospital/department_list.html', dept)