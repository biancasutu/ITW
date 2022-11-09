from django.urls import path

from userextend import views

urlpatterns = [
    path('sign-up/', views.UserCreateView.as_view(), name='sign_up')
]