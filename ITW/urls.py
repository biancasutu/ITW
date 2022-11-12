"""ITW URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from players import urls
from userextend import views
from userextend.forms import AuthenticationNewForm, PasswordResetNewForm, SetPasswordNewForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('players/', include('players.urls')),  # include numele aplicatiei + python file (in acest caz este urls),
    path('store/', include('store.urls')),
    path('accessories/', include('store.accessories_url')),
    path("login/", views.LoginView.as_view(form_class=AuthenticationNewForm), name="login"),
    path("password_reset/", views.PasswordResetView.as_view(form_class=PasswordResetNewForm), name="password_reset"),
    path(
        "reset/<uidb64>/<token>/",
        views.PasswordResetConfirmView.as_view(form_class=SetPasswordNewForm),
        name="password_reset_confirm"
    ),
    path('', include('django.contrib.auth.urls')),
    path('', include('userextend.urls')),
    path('cart/', include('cart.urls'))
]
