from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.

# /パスでアクセスしたとき用のリダイレクト
def index(request):
    return redirect('/budgets/')

# 一覧画面
def top(request):
    return HttpResponse('Hello World')
