from django.http import HttpResponse
from django.shortcuts import render
from django.forms.models import model_to_dict
from .models import Usagedb
import json
from django.views.decorators.csrf import csrf_exempt
from django.template.context_processors import csrf
# Create your views here.


# 接收请求体数据
@csrf_exempt
def create_receive(request):
    body_dict=json.loads(request.body)
    #向表中新增数据
    Usagedb.objects.create(send_time=body_dict['current_time'],cpu_ratio=body_dict['cpu_use_ratio'],memory_ratio=body_dict['memory_ratio'])
    return HttpResponse("hello body!")

