# 用来写展示函数的，大概是吧server搬到这边来了吧
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
from django.shortcuts import render
from deepcube.tools import getResults
from django import forms
import json
import ast
import os


def index(request):
    if request.method == 'GET':
        return render(request, 'mofang.html')

@csrf_exempt
def initState(request):
    if request.method =='POST':
        
        with open(os.path.join(os.getcwd(), 'deepcube/initState.json'), 'r') as f:
            result = json.load(f)
        print(result)
        return HttpResponse(json.dumps(result), content_type="application/json")   # jsonify(result)     # 这是这样from flask import jsonify用的，返回json格式的数据

@csrf_exempt        
def solve(request):
    if request.method == 'POST':
        data = request.POST.copy()
        print("computing...")
        state = []
        data['state'] = ast.literal_eval(data['state'])
        for i in data['state']:
            state.append(int(i))
        result = getResults(state)
        print("complete!")
        return HttpResponse(json.dumps(result), content_type="application/json")   # jsonify(result)     # 这是这样from flask import jsonify用的，要改
        