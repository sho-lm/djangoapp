from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm


# 疎通用
def test(request):
    return render(request, 'accounts/test.html')

class IndexView(TemplateView):
    """ ホームビュー """
    template_name = "index.html"

class SignupView(CreateView):
    """ユーザー登録用ビュー"""
    form_class = SignUpForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:test') # ユーザー作成後のリダイレクト先
    
    def form_valid(self, form):
        # ユーザー作成後にそのままログイン状態する設定
        response = super().form_valid(form)
        account_id = form.cleaned_data.get('account_id')
        password = form.cleaned_data.get('password')
        user = authenticate(account_id=account_id, password=password)
        login(self.request, user)
        return response