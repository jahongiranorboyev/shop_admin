from django.contrib.auth import views as auth_views
from django.urls import path
from .views import CustomLoginView, CustomLogoutView, RegisterView, LoginPageView


app_name = 'authentications'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('register/login', LoginPageView.as_view(), name='register-login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),




    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]

