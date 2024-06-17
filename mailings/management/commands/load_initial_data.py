from django.core.management import BaseCommand
from mailings.models import Mailing, Message, Client
from blog.models import BlogPost
from django.contrib.auth.models import Group


class Command(BaseCommand):
    help = 'Load initial data into the database'

    def handle(self, *args, **kwargs):
        # Создание групп
        groups = [
            {'name': 'managers'},
            {'name': 'users'},
        ]

        groups_for_create = []
        for group_item in groups:
            groups_for_create.append(
                Group(**group_item)
            )
        Group.objects.bulk_create(groups_for_create)

        # Создание клиентов
        clients = [
            {'name': 'John', 'surname': 'Doe', 'email': 'john@example.com', 'comments': 'Regular client'},
            {'name': 'Jane', 'surname': 'Smith', 'email': 'jane@example.com', 'comments': 'New client'},
        ]

        clients_for_create = []
        for client_item in clients:
            clients_for_create.append(
                Client(**client_item)
            )
        Client.objects.bulk_create(clients_for_create)

        # Создание сообщений
        messages = [
            {'subject': 'Welcome', 'body': 'Welcome to our service!'},
            {'subject': 'Update', 'body': 'Here is an update on our services.'},
        ]

        messages_for_create = []
        for message_item in messages:
            messages_for_create.append(
                Message(**message_item)
            )
        Message.objects.bulk_create(messages_for_create)

        # Создание рассылок
        mailings = [
            {
                'name': 'Morning Update',
                'start_date_time': '2024-06-17T08:00:00Z',
                'periodicity': 'daily',
                'status': 'created',
                'message_id': 1,
                'owner_id': 1
            },
        ]

        mailings_for_create = []
        for mailing_item in mailings:
            mailings_for_create.append(
                Mailing(**mailing_item)
            )
        Mailing.objects.bulk_create(mailings_for_create)

        # Добавление клиентов к рассылкам
        mailing1 = Mailing.objects.get(id=1)
        mailing1.clients.add(*Client.objects.all())

        # Создание статей блога
        blog_posts = [
            {'title': 'How to Use Our Service', 'content': '<p>Here is how you can use our service...</p>',
             'publication_date': '2024-06-17', 'views': 10},
            {'title': 'Benefits of Email Marketing', 'content': '<p>Email marketing is beneficial because...</p>',
             'publication_date': '2024-06-18', 'views': 15},
        ]

        blog_posts_for_create = []
        for blog_post_item in blog_posts:
            blog_posts_for_create.append(
                BlogPost(**blog_post_item)
            )
        BlogPost.objects.bulk_create(blog_posts_for_create)

        self.stdout.write(self.style.SUCCESS('Initial data loaded successfully'))
