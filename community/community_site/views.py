from django.views import generic
from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from .forms import UserCreateForm, LoginForm, MyPasswordChangeForm
from django.contrib.auth import login, authenticate, views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class Index(LoginRequiredMixin, generic.TemplateView):

    template_name = 'registration/top.html'


class Login(views.LoginView):
    def post(self, request, *args, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('../top')
        return render(request, 'login.html', {'form': form, })

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        return render(request, 'login.html', {'form': form, })

'''

class Logout(LoginRequiredMixin, views.LogoutView):
    """ログアウトページ"""
    template_name = 'top.html'
'''

'''


class Login(views.LoginView):
    def post(self, request, *args, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User.objects.get(username=username, password=password)
            login(request, user)
            return redirect('../')
        return render(request, 'top.html', {'form': form, })

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        return render(request, 'top.html', {'form': form, })
'''


class Create(generic.CreateView):
    def post(self, request, *args, **kwargs):
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            '''
            # フォームから'username'を読み取る
            username = form.cleaned_data.get('username')
            # フォームから'password1'を読み取る
            password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)
            login(request, user)
            '''
            return redirect('../login')
        return render(request, 'create.html', {'form': form, })

    def get(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        return render(request, 'create.html', {'form': form, })


class SmartListView(ListView):
    template_name = 'jj.html'
    model = Post


'''
class PasswordChange(generic.TemplateView):
    def password_change(request):
        template_name = 'password_change.html'
        form = MyPasswordChangeForm(user=request.user)
        context = {
            'form': form,
        }
        return render(request, template_name, context)


    # パスワードの変更を保存する処理
    def post(self, request, *args, **kwargs):
        form = MyPasswordChangeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('../login')
'''


class PasswordChange(views.PasswordChangeView):
    """パスワード変更ビュー"""
    form_class = MyPasswordChangeForm
    success_url = reverse_lazy('login')
    template_name = 'registration/password_change.html'


class Chat(generic.TemplateView):
    template_name = 'registration/chat.html'

    def get(self, request, **kwargs):
        ctx = {
            'username': self.request.user.username
        }
        return self.render_to_response(ctx)
