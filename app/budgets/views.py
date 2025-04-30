from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.

# /パスでアクセスしたとき用のリダイレクト
def index(request):
    return redirect('/budgets/')

# 一覧画面(トップページ)
def top(request):
    context = {} # 収支の取得結果などを入れる
    return render(request, 'budgets/top.html', context)
