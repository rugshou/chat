from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
index_view = views.Index.as_view()

urlpatterns = [

    path('top/', views.Index.as_view(), name='top'),
    path('login/', views.Login.as_view(), name='login'),
    path('create/', views.Create.as_view(), name='create'),
    path('for/', views.SmartListView.as_view(), name='for'),
    path('aa/', views.Index.as_view(), name='aa'),
    path('password_change/', views.PasswordChange.as_view(), name='password_change'),
    path('', login_required(views.Chat.as_view()), name='chat'),
]
