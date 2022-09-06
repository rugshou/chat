from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm


class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'account_name text_box account_box'
        self.fields['password1'].widget.attrs['class'] = 'account_name text_box account_box'
        self.fields['password2'].widget.attrs['class'] = 'account_name text_box account_box'
        self.fields['username'].widget.attrs['id'] = 'username'
        self.fields['password1'].widget.attrs['id'] = 'password'
        self.fields['password2'].widget.attrs['id'] = 'passwordConfirm'
        self.fields['password1'].widget.attrs['placeholder'] = '半角英数字8文字以上'
        self.fields['password2'].widget.attrs['placeholder'] = 'パスワード確認用'


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'


class MyPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs['class'] = 'account_name text_box account_box'
        self.fields['new_password1'].widget.attrs['class'] = 'account_name text_box account_box'
        self.fields['new_password2'].widget.attrs['class'] = 'account_name text_box account_box'
        self.fields['new_password1'].widget.attrs['placeholder'] = '半角英数字8文字以上'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'パスワード確認用'
        self.fields['old_password'].widget.attrs['id'] = 'old_password'
        self.fields['new_password1'].widget.attrs['id'] = 'new_password1'
        self.fields['new_password2'].widget.attrs['id'] = 'new_password2'
