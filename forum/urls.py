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
    path('boards/<int:pk>/topics/<topic_pk>', board_view.topic_posts, name='topic_posts'),
    path('boards/<int:pk>/topics/<topic_pk>/reply', board_view.reply_topic, name='reply_topic'),
    path('boards/<int:pk>/topics/<int:topic_pk>/posts/<int:post_pk>/edit/',
         board_view.PostUpdateView.as_view(), name='edit_post'),

    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('signup/', account_view.signup, name='signup'),
    path('reset/', auth_view.PasswordResetView.as_view(
        template_name='password_reset.html',
        email_template_name='password_reset_email.html',
        subject_template_name='password_reset_subject.txt'
    ), name='password_reset'),
    path('reset/done/', auth_view.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
         auth_view.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/complete/',
         auth_view.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),
    path('password_change/', auth_view.PasswordChangeView.as_view(template_name='password_change.html'),
         name='password_change'),
    path('password_change/done/', auth_view.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
         name='password_change_done'),
]
