# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from django.db.models import Q
from django.core import serializers
import json


from cmdb.models import *

# Create your views here.

@require_http_methods(["GET"])
def add_computer_resource(request):
    response={}
    try:
        res = cmdb_ci(name=request.GET.get('name'))
        response['msg'] = 'success'
        response['error_num'] = 1
        print(res)
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def show_List(request):
    response = {}
    try:
        res = cmdb_ci.objects.all()
        response['list'] = json.load(serializers.serialize("json",res))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as  e:
        response['msg'] =str(e)
        response['error_num'] = 1
    return JsonResponse(response)

