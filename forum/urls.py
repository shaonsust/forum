"""forum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth import views as auth_view
from django.urls import path
from boards import views as board_view
from accounts import views as account_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', board_view.home, name='home'),
    path('board_topics/<int:board_id>', board_view.board_topics, name='board_topics'),
    path('boards/new_topic/<int:board_id>', board_view.new_topic, name='new_topic'),
    path('signup/', account_view.signup, name='signup'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login')
]
