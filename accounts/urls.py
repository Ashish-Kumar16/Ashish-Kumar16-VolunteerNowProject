# accounts/urls.py
from django.urls import path
from .views import RegisterView, LoginView, ChangePasswordView, ResetPasswordView, IsAuthenticatedView, VerifyOtpView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('is-authenticated/', IsAuthenticatedView.as_view()),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset_password'),
    path('verify-otp/', VerifyOtpView.as_view(), name='verify_otp'),
    # path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
