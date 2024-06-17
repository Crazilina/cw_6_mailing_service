import random
from .services import get_cached_home_data
from config import settings

from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .models import Client, Message, Mailing, MailingAttempt
from .forms import ClientForm, MessageForm, MailingForm


class HomeListView(ListView):
    model = Client
    template_name = 'mailings/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cached_data = get_cached_home_data()

        context.update(cached_data)
        context['user'] = self.request.user
        return context


# Clients
class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'mailings/client_list.html'
    context_object_name = 'clients'

    def get_queryset(self):
        return Client.objects.filter(owner=self.request.user).order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['system_messages'] = messages.get_messages(self.request)
        return context


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'mailings/client_form.html'
    success_url = reverse_lazy('mailings:client_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, f'Client "{form.instance.name} {form.instance.surname}" successfully created.')
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['system_messages'] = messages.get_messages(self.request)
        return context


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'mailings/client_form.html'
    success_url = reverse_lazy('mailings:client_list')

    def get_queryset(self):
        return Client.objects.filter(owner=self.request.user)

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Client "{form.instance.name} {form.instance.surname}" successfully updated.')
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['system_messages'] = messages.get_messages(self.request)
        return context


class ClientDetailView(DetailView):
    model = Client
    template_name = 'mailings/client_detail.html'
    context_object_name = 'client'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['system_messages'] = messages.get_messages(self.request)
        return context


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = 'mailings/client_confirm_delete.html'
    success_url = reverse_lazy('mailings:client_list')

    def get_queryset(self):
        return Client.objects.filter(owner=self.request.user)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, f'Client "{self.object.name} {self.object.surname}" successfully deleted.')
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['system_messages'] = messages.get_messages(self.request)
        return context


# Messages
class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'mailings/message_list.html'
    context_object_name = 'messages'

    def get_queryset(self):
        return Message.objects.filter(owner=self.request.user).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['system_messages'] = messages.get_messages(self.request)
        return context


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'mailings/message_form.html'
    success_url = reverse_lazy('mailings:message_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, f'Message "{form.instance.subject}" successfully created.')
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['system_messages'] = messages.get_messages(self.request)
        return context


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    template_name = 'mailings/message_form.html'
    success_url = reverse_lazy('mailings:message_list')

    def get_queryset(self):
        return Message.objects.filter(owner=self.request.user)

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Message {form.instance.subject} successfully updated.')
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['system_messages'] = messages.get_messages(self.request)
        return context


class MessageDetailView(DetailView):
    model = Message
    template_name = 'mailings/message_detail.html'
    context_object_name = 'message'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['system_messages'] = messages.get_messages(self.request)
        return context


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    template_name = 'mailings/message_confirm_delete.html'
    success_url = reverse_lazy('mailings:message_list')

    def get_queryset(self):
        return Message.objects.filter(owner=self.request.user)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, f'Message {self.object.subject} successfully deleted.')
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['system_messages'] = messages.get_messages(self.request)
        return context


# Mailings
class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing
    template_name = 'mailings/mailing_list.html'
    context_object_name = 'mailings'

    def get_queryset(self):
        return Mailing.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['system_messages'] = messages.get_messages(self.request)
        return context


class ActiveMailingListView(ListView):
    model = Mailing
    template_name = 'mailings/active_mailing_list.html'
    context_object_name = 'mailings'

    def get_queryset(self):
        return Mailing.objects.filter(status='started')


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mailings/mailing_form.html'
    success_url = reverse_lazy('mailings:mailing_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, f'Mailing "{form.instance}" successfully created.')
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['system_messages'] = messages.get_messages(self.request)
        return context


class MailingUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mailings/mailing_form.html'
    success_url = reverse_lazy('mailings:mailing_list')
    permission_required = 'mailings.change_mailing'

    def get_queryset(self):
        return Mailing.objects.filter(owner=self.request.user)

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Mailing {form.instance.name} successfully updated.')
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['system_messages'] = messages.get_messages(self.request)
        return context


class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailing
    template_name = 'mailings/mailing_detail.html'
    context_object_name = 'mailing'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mailing_name'] = self.object.name
        context['message_body'] = self.object.message.body
        return context


class MailingDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Mailing
    template_name = 'mailings/mailing_confirm_delete.html'
    success_url = reverse_lazy('mailings:mailing_list')
    permission_required = 'mailings.delete_mailing'

    def get_queryset(self):
        return Mailing.objects.filter(owner=self.request.user)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, f'Mailing {self.object.name} successfully deleted.')
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['system_messages'] = messages.get_messages(self.request)
        return context


class MailingAttemptListView(LoginRequiredMixin, ListView):
    model = MailingAttempt
    template_name = 'mailings/mailing_attempt_list.html'
    context_object_name = 'mailing_attempts'

    def get_queryset(self):
        return MailingAttempt.objects.select_related('mailing').all().order_by('-attempt_date_time')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['system_messages'] = messages.get_messages(self.request)
        return context


class MailingAttemptDetailView(LoginRequiredMixin, DetailView):
    model = MailingAttempt
    template_name = 'mailings/mailing_attempt_detail.html'
    context_object_name = 'attempt'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['system_messages'] = messages.get_messages(self.request)
        return context


@permission_required('mailings.can_disable_mailing')
def toggle_mailing_status(request, mailing_id):
    mailing = get_object_or_404(Mailing, id=mailing_id)

    if mailing.status == Mailing.STARTED:
        mailing.status = Mailing.COMPLETED
        messages.success(request, f'Mailing "{mailing.name}" has been completed.')
    else:
        mailing.status = Mailing.STARTED
        messages.success(request, f'Mailing "{mailing.name}" has been activated.')

    mailing.save()
    return redirect('mailings:mailing_list')
