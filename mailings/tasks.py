import smtplib
import pytz
from apscheduler.schedulers.background import BackgroundScheduler
from django.core.mail import send_mail
from django.conf import settings
from django_apscheduler.jobstores import DjangoJobStore
from .models import Mailing, MailingAttempt
from datetime import datetime


def send_mailing():
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    mailings = Mailing.objects.filter(start_date_time__lte=current_datetime, status__in=['created', 'started'])

    for mailing in mailings:
        last_attempt = MailingAttempt.objects.filter(mailing=mailing).order_by('-attempt_date_time').first()
        if last_attempt:
            if mailing.periodicity == 'daily' and (current_datetime - last_attempt.attempt_date_time).days < 1:
                continue
            if mailing.periodicity == 'weekly' and (current_datetime - last_attempt.attempt_date_time).days < 7:
                continue
            if mailing.periodicity == 'monthly' and (current_datetime - last_attempt.attempt_date_time).days < 30:
                continue
        try:
            send_mail(
                subject=mailing.message.subject,
                message=mailing.message.body,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[client.email for client in mailing.clients.all()],
                fail_silently=False
            )
            MailingAttempt.objects.create(
                mailing=mailing,
                status='success',
                server_response="Email sent successfully"
            )
            mailing.status = 'completed'
            mailing.save()
        except smtplib.SMTPException as e:
            MailingAttempt.objects.create(
                mailing=mailing,
                status='failed',
                server_response=str(e)
            )


def start_scheduler(sender, **kwargs):
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    scheduler.add_job(send_mailing, 'interval', seconds=20, id='send_mailing', replace_existing=True)
    scheduler.start()
