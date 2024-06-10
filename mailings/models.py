from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    surname = models.CharField(max_length=255, verbose_name="Фамилия")
    email = models.EmailField(unique=True, verbose_name="Email")
    comments = models.TextField(**NULLABLE, verbose_name="Комментарий")

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return f"{self.name} {self.surname} ({self.email})"


class Message(models.Model):
    subject = models.CharField(max_length=255, verbose_name="Тема письма")
    body = models.TextField(verbose_name="Тело письма")

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

    def __str__(self):
        return self.subject


class Mailing(models.Model):
    DAILY = 'daily'
    WEEKLY = 'weekly'
    MONTHLY = 'monthly'
    PERIODICITY_CHOICES = [
        (DAILY, 'Ежедневно'),
        (WEEKLY, 'Еженедельно'),
        (MONTHLY, 'Ежемесячно'),
    ]

    CREATED = 'created'
    STARTED = 'started'
    COMPLETED = 'completed'
    STATUS_CHOICES = [
        (CREATED, 'Создана'),
        (STARTED, 'Запущена'),
        (COMPLETED, 'Завершена'),
    ]

    name = models.CharField(max_length=255, verbose_name="Имя рассылки")
    start_date_time = models.DateTimeField(verbose_name="Дата и время первой отправки")
    periodicity = models.CharField(max_length=10, choices=PERIODICITY_CHOICES, verbose_name="Периодичность")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=CREATED, verbose_name="Статус")
    message = models.OneToOneField(Message, on_delete=models.CASCADE, verbose_name="Сообщение")
    clients = models.ManyToManyField(Client, verbose_name="Клиенты")

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"

    def __str__(self):
        return f"Mailing {self.name} - {self.status}"


class MailingAttempt(models.Model):
    SUCCESS = 'success'
    FAILED = 'failed'
    STATUS_CHOICES = [
        (SUCCESS, 'Успешно'),
        (FAILED, 'Неудачно'),
    ]

    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name="Рассылка")
    attempt_date_time = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время попытки")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name="Статус попытки")
    server_response = models.TextField(**NULLABLE, verbose_name="Ответ почтового сервера")

    class Meta:
        verbose_name = "Попытка рассылки"
        verbose_name_plural = "Попытки рассылки"

    def __str__(self):
        return f"Attempt {self.pk} - {self.status}"
