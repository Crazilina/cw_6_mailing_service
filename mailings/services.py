from django.conf import settings
from django.core.cache import cache
from mailings.models import Mailing, Client
from blog.models import BlogPost

import random


def get_cached_home_data():
    if settings.CACHE_ENABLED:
        # Кеширование общего количества рассылок
        total_mailings = cache.get('total_mailings')
        if total_mailings is None:
            total_mailings = Mailing.objects.count()
            cache.set('total_mailings', total_mailings, 60 * 15)  # Кешируем на 15 минут

        # Кеширование активных рассылок
        active_mailings = cache.get('active_mailings')
        if active_mailings is None:
            active_mailings = Mailing.objects.filter(status=Mailing.STARTED).count()
            cache.set('active_mailings', active_mailings, 60 * 15)

        # Кеширование уникальных клиентов
        unique_clients = cache.get('unique_clients')
        if unique_clients is None:
            unique_clients = Client.objects.distinct().count()
            cache.set('unique_clients', unique_clients, 60 * 15)

        # Кеширование случайных статей блога
        random_blog_posts = cache.get('random_blog_posts')
        if random_blog_posts is None:
            all_blog_posts = list(BlogPost.objects.all())
            random_blog_posts = random.sample(all_blog_posts, min(3, len(all_blog_posts)))
            cache.set('random_blog_posts', random_blog_posts, 60 * 15)
    else:
        total_mailings = Mailing.objects.count()
        active_mailings = Mailing.objects.filter(status=Mailing.STARTED).count()
        unique_clients = Client.objects.distinct().count()
        all_blog_posts = list(BlogPost.objects.all())
        random_blog_posts = random.sample(all_blog_posts, min(3, len(all_blog_posts)))

    return {
        'total_mailings': total_mailings,
        'active_mailings': active_mailings,
        'unique_clients': unique_clients,
        'random_blog_posts': random_blog_posts,
    }
