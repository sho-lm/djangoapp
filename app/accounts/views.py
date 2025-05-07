from django.shortcuts import render

# Create your views here.

# 疎通用
def test(request):
    return render(request, 'accounts/test.html')
