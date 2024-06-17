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
    list_display = ('name', 'start_date_time', 'periodicity', 'status')
    actions = ['disable_mailings', 'enable_mailings']
    list_filter = ('periodicity', 'status')

    def disable_mailings(self, request, queryset):
        queryset.update(status=Mailing.COMPLETED)
        self.message_user(request, "Selected mailings have been disabled.")

    disable_mailings.short_description = "Disable selected mailings"

    def enable_mailings(self, request, queryset):
        queryset.update(status=Mailing.STARTED)
        self.message_user(request, "Selected mailings have been enabled.")

    enable_mailings.short_description = "Enable selected mailings"


@admin.register(MailingAttempt)
class MailingAttemptAdmin(admin.ModelAdmin):
    list_display = ('mailing', 'attempt_date_time', 'status')
    search_fields = ('status',)
    list_filter = ('status', 'attempt_date_time')
