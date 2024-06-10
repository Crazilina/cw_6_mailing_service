from django.contrib import admin
from .models import Client, Message, Mailing, MailingAttempt


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email')
    search_fields = ('name', 'surname', 'email')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject',)
    search_fields = ('subject',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('start_date_time', 'periodicity', 'status')
    search_fields = ('status',)
    list_filter = ('periodicity', 'status')


@admin.register(MailingAttempt)
class MailingAttemptAdmin(admin.ModelAdmin):
    list_display = ('mailing', 'attempt_date_time', 'status')
    search_fields = ('status',)
    list_filter = ('status', 'attempt_date_time')
