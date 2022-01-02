from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView

urlpatterns = [
    path('register/',views.registerView,name='register'),
    path('login/',views.loginView,name='login'),
    path('logout/',views.logoutView,name='logout'),
    path('otp/',views.otpVerifyView,name='otp_verify'),
    path('password_reset/', PasswordResetView.as_view(template_name='AccountApp/passwordReset.html'), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='AccountApp/passwordresetDone.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name="AccountApp/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='AccountApp/password_resetComplete.html'), name='password_reset_complete'),
]