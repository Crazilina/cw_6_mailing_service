import secrets
import random
import string

from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, FormView, ListView

from users.forms import UserRegisterForm, PasswordResetRequestForm
from users.models import User
from django.contrib import messages
from config.settings import EMAIL_HOST_USER


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False  # Аккаунт пока не активен до подтверждения по email
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        send_mail(
            subject='Подтверждение почты',
            message=f'Привет! Перейди по ссылке для подтверждения почты {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.token = None
    user.save()
    return redirect(reverse("users:login"))


class PasswordResetRequestView(FormView):
    template_name = 'users/password_reset_form.html'
    form_class = PasswordResetRequestForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        user = User.objects.filter(email=email).first()
        if user:
            new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            user.password = make_password(new_password)
            user.save()
            send_mail(
                subject='Восстановление пароля',
                message=f'Ваш новый пароль: {new_password}',
                from_email=EMAIL_HOST_USER,
                recipient_list=[user.email]
            )
            return super().form_valid(form)
        else:
            # Если пользователь не найден, добавляем ошибку в форму
            form.add_error('email', 'Пользователь с таким email не найден.')
            return self.form_invalid(form)


class UserListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'users'
    permission_required = 'users.view_user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['system_messages'] = messages.get_messages(self.request)
        return context


@login_required
@permission_required('users.can_block_user')
def toggle_user_active(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if user.is_superuser:
        messages.error(request, "You cannot block or unblock a superuser.")
    else:
        if user.is_active:
            user.is_active = False
            messages.success(request, f'User {user.email} has been blocked.')
        else:
            user.is_active = True
            messages.success(request, f'User {user.email} has been unblocked.')
        user.save()
    return redirect('users:user_list')
