from django.urls import path, include

from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.customLogin, name='login'),
    path('logout', views.customLogout, name='logout'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),

    path('profile/<username>', views.profile, name='profile'),
    # path("password_change", views.password_change, name="password_change"),
    # path("password_reset", views.password_reset_request, name="password_reset"),
    # path('reset/<uidb64>/<token>', views.passwordResetConfirm, name='password_reset_confirm'),
    # path('social/signup/', views.signup_redirect, name='signup_redirect'),
]
