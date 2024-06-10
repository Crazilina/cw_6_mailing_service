from django.urls import path
from mailings.views import (
    HomeListView,
    ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView,
    MessageListView, MessageDetailView, MessageCreateView, MessageUpdateView, MessageDeleteView,
    MailingListView, MailingDetailView, MailingCreateView, MailingUpdateView, MailingDeleteView,
    MailingAttemptListView, MailingAttemptDetailView,
)

app_name = 'mailings'

urlpatterns = [
    # Маршрут для главной страницы
    path('', HomeListView.as_view(), name='home'),

    # Clients
    path('clients/', ClientListView.as_view(), name='client_list'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('clients/create/', ClientCreateView.as_view(), name='client_create'),
    path('clients/<int:pk>/update/', ClientUpdateView.as_view(), name='client_update'),
    path('clients/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),

    # Messages
    path('messages/', MessageListView.as_view(), name='message_list'),
    path('messages/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('messages/create/', MessageCreateView.as_view(), name='message_create'),
    path('messages/<int:pk>/update/', MessageUpdateView.as_view(), name='message_update'),
    path('messages/<int:pk>/delete/', MessageDeleteView.as_view(), name='message_delete'),

    # Mailings
    path('mailings/', MailingListView.as_view(), name='mailing_list'),
    path('mailings/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailings/create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailings/<int:pk>/update/', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailings/<int:pk>/delete/', MailingDeleteView.as_view(), name='mailing_delete'),

    # Attempts
    path('mailing_attempts/', MailingAttemptListView.as_view(), name='mailing_attempt_list'),
    path('mailing_attempts/<int:pk>/', MailingAttemptDetailView.as_view(), name='mailing_attempt_detail'),
]
