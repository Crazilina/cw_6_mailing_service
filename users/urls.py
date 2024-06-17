from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, email_verification, PasswordResetRequestView, UserListView, toggle_user_active

app_name = UsersConfig.name

urlpatterns = [
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/<int:user_id>/toggle/', toggle_user_active, name='toggle_user_active'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),
    path('password-reset/', PasswordResetRequestView.as_view(), name='password_reset'),
]
