from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from .views import RegisterView, VerifyEmail, LoginAPIView, PasswordTokenCheckAPI, RequestPasswordResetEmail, SetNewPasswordAPIView, LogoutAPIView, AuthUserAPIView


urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    path('user/', AuthUserAPIView.as_view(), name="user"),
    path('request-reset-email/', RequestPasswordResetEmail.as_view(), name='request-reset-email'),
    path('password-reset/<uidb64>/<token>/', PasswordTokenCheckAPI.as_view(), name="password-reset-confirm"),
    path('password-reset-complete', SetNewPasswordAPIView.as_view(), name="password-reset-complete"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]