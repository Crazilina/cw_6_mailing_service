from django import forms
from mailings.models import Client, Message, Mailing


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'surname', 'email', 'comments']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['subject', 'body']


class MailingForm(forms.ModelForm):
    start_date_time = forms.DateTimeField(widget=forms.TextInput(attrs={
        'id': 'datetimepicker1',
        'name': 'start_date_time',
        'class': 'form-control datetimepicker-input col-md-3',
        'data-target': '#datetimepicker1'
    }))

    class Meta:
        model = Mailing
        fields = ['name', 'start_date_time', 'periodicity', 'status', 'message', 'clients']
        widgets = {
            'clients': forms.CheckboxSelectMultiple(attrs={'id': 'id_clients', 'name': 'clients'})
        }
