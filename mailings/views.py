from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Client, Message, Mailing, MailingAttempt
from .forms import ClientForm, MessageForm, MailingForm


class HomeListView(ListView):
    model = Client
    template_name = 'mailings/home.html'
    context_object_name = 'clients'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clients'] = Client.objects.order_by('name')
        context['messages'] = Message.objects.order_by('-id')
        context['mailings'] = Mailing.objects.order_by('-id')
        context['mailing_attempts'] = MailingAttempt.objects.order_by('-attempt_date_time')
        context['recent_clients'] = Client.objects.order_by('-id')[:5]
        context['recent_messages'] = Message.objects.order_by('-id')[:5]
        context['recent_mailings'] = Mailing.objects.order_by('-id')[:5]
        context['user'] = self.request.user
        return context


# Clients
class ClientListView(ListView):
    model = Client
    template_name = 'mailings/client_list.html'
    context_object_name = 'clients'

    def get_queryset(self):
        return Client.objects.order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['system_messages'] = messages.get_messages(self.request)
        return context


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'mailings/client_form.html'
    success_url = reverse_lazy('mailings:client_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Client "{form.instance.name} {form.instance.surname}" successfully created.')
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['system_messages'] = messages.get_messages(self.request)
        return context


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'mailings/client_form.html'
    success_url = reverse_lazy('mailings:client_list')

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


class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'mailings/client_confirm_delete.html'
    success_url = reverse_lazy('mailings:client_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, f'Client {self.object.name} {self.object.surname} successfully deleted.')
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['system_messages'] = messages.get_messages(self.request)
        return context


# Messages
class MessageListView(ListView):
    model = Message
    template_name = 'mailings/message_list.html'
    context_object_name = 'messages'

    def get_queryset(self):
        return Message.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['system_messages'] = messages.get_messages(self.request)
        return context


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'mailings/message_form.html'
    success_url = reverse_lazy('mailings:message_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Message {form.instance.subject} successfully created.')
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['system_messages'] = messages.get_messages(self.request)
        return context


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    template_name = 'mailings/message_form.html'
    success_url = reverse_lazy('mailings:message_list')

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


class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'mailings/message_confirm_delete.html'
    success_url = reverse_lazy('mailings:message_list')

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
class MailingListView(ListView):
    model = Mailing
    template_name = 'mailings/mailing_list.html'
    context_object_name = 'mailings'

    def get_queryset(self):
        return Mailing.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['system_messages'] = messages.get_messages(self.request)
        return context


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mailings/mailing_form.html'
    success_url = reverse_lazy('mailings:mailing_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Mailing {form.instance.name} successfully created.')
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['system_messages'] = messages.get_messages(self.request)
        return context


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mailings/mailing_form.html'
    success_url = reverse_lazy('mailings:mailing_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Mailing {form.instance.name} successfully updated.')
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['system_messages'] = messages.get_messages(self.request)
        return context


class MailingDetailView(DetailView):
    model = Mailing
    template_name = 'mailings/mailing_detail.html'
    context_object_name = 'mailing'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mailing_name'] = self.object.name
        context['message_body'] = self.object.message.body
        return context


class MailingDeleteView(DeleteView):
    model = Mailing
    template_name = 'mailings/mailing_confirm_delete.html'
    success_url = reverse_lazy('mailings:mailing_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, f'Mailing {self.object.name} successfully deleted.')
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['system_messages'] = messages.get_messages(self.request)
        return context


class MailingAttemptListView(ListView):
    model = MailingAttempt
    template_name = 'mailings/mailing_attempt_list.html'
    context_object_name = 'mailing_attempts'

    def get_queryset(self):
        return MailingAttempt.objects.select_related('mailing').all().order_by('-attempt_date_time')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['system_messages'] = messages.get_messages(self.request)
        return context


class MailingAttemptDetailView(DetailView):
    model = MailingAttempt
    template_name = 'mailings/mailing_attempt_detail.html'
    context_object_name = 'attempt'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['system_messages'] = messages.get_messages(self.request)
        return context


