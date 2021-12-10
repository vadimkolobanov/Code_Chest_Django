from random import randint

from django.core.management import BaseCommand

from users.models import User
from main.models import Project, UserProjectCompleted


class Command(BaseCommand):
    def handle(self, *args, **options):
        users_key_products = [i for i in UserProjectCompleted.objects.all()]

        for key in users_key_products:
            try:
                user, project = key.user, key.project
                key.delete()
                self.stdout.write(self.style.SUCCESS(f'Пользователь \"{user}\", покинул проект \"{project}\"!'))
            except Exception as error:
                self.stdout.write(self.style.ERROR(
                    f'Пользователь \"{user}\", остался на проекте \"{project}\"! \n Error: {error} \n {"-" * 5}'))

        user_list = [i for i in User.objects.all()]

        for user in user_list:
            try:
                if user.id == 1 or user.username == 'admin':
                    continue
                else:
                    name = user.username
                    user.delete()
                    self.stdout.write(self.style.SUCCESS(f'User \"{name}\" deleted successfully!'))
            except Exception as error:
                self.stdout.write(self.style.ERROR(f'User \"{name}\" not deleted! \n Error: {error} \n {"-" * 5}'))

        project_list = [i for i in Project.objects.all()]

        for project in project_list:
            try:
                name = project.name
                project.delete()
                self.stdout.write(self.style.SUCCESS(f'Project \"{name}\" deleted successfully!'))
            except Exception as error:
                self.stdout.write(self.style.ERROR(f'Project \"{name}\" not deleted! \n Error: {error} \n {"-" * 5}'))
