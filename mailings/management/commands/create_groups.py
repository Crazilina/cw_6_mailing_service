from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = 'Create Manager group and assign permissions'

    def handle(self, *args, **kwargs):
        # Создание группы "Manager"
        manager_group, created = Group.objects.get_or_create(name='Manager')
        if created:
            self.stdout.write(self.style.SUCCESS(f'Group "Manager" created'))
        else:
            self.stdout.write(self.style.WARNING(f'Group "Manager" already exists'))

        # Получение разрешений
        permissions = [
            'can_disable_mailing',  # Разрешение для отключения рассылок
            'view_user',  # Разрешение для просмотра пользователей
            'can_block_user',  # Разрешение для блокировки пользователей
            'view_mailing'  # Разрешение для просмотра рассылок
        ]

        for perm_codename in permissions:
            try:
                permission = Permission.objects.get(codename=perm_codename)
                manager_group.permissions.add(permission)
                self.stdout.write(self.style.SUCCESS(f'Added "{perm_codename}" permission to "Manager" group'))
            except Permission.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Permission "{perm_codename}" not found'))

        self.stdout.write(self.style.SUCCESS('All specified permissions assigned to Manager group'))
