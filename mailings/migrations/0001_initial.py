# Generated by Django 5.0.6 on 2024-06-08 16:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('surname', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Контактный email')),
                ('comments', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255, verbose_name='Тема письма')),
                ('body', models.TextField(verbose_name='Тело письма')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date_time', models.DateTimeField(verbose_name='Дата и время первой отправки')),
                ('periodicity', models.CharField(choices=[('daily', 'Ежедневно'), ('weekly', 'Еженедельно'), ('monthly', 'Ежемесячно')], max_length=10, verbose_name='Периодичность')),
                ('status', models.CharField(choices=[('created', 'Создана'), ('started', 'Запущена'), ('completed', 'Завершена')], default='created', max_length=10, verbose_name='Статус')),
                ('clients', models.ManyToManyField(to='mailings.client', verbose_name='Клиенты')),
                ('message', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mailings.message', verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
            },
        ),
        migrations.CreateModel(
            name='MailingAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attempt_date_time', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время попытки')),
                ('status', models.CharField(choices=[('success', 'Успешно'), ('failed', 'Неудачно')], max_length=10, verbose_name='Статус попытки')),
                ('server_response', models.TextField(blank=True, null=True, verbose_name='Ответ почтового сервера')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailings.mailing', verbose_name='Рассылка')),
            ],
            options={
                'verbose_name': 'Попытка рассылки',
                'verbose_name_plural': 'Попытки рассылки',
            },
        ),
    ]
