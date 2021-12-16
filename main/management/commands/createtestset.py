from random import randint

from django.core.management import BaseCommand

from users.models import User
from main.models import Project, UserProjectCompleted


class Command(BaseCommand):
    def handle(self, *args, **options):
        user_list = [
            {'username':'Ivan', 'email':'ivan@example.ru', 'password':'1'},
            {'username':'Mark', 'email':'mark@example.ru', 'password':'1'},
            {'username':'Vadim', 'email':'vadim@example.ru', 'password':'1'},
            {'username':'Gera', 'email':'gera@example.ru', 'password':'1'},
        ]

        for user in user_list:
            try:
                User.objects.create_user(username=user['username'], email=user['email'], password=user['password'])
                self.stdout.write(self.style.SUCCESS(f'User \"{user["username"]}\" created successfully!'))
            except Exception as error:
                self.stdout.write(self.style.ERROR(f'User \"{user["username"]}\" not created! \n Error: {error} \n {"-" * 5}'))

        project_list = [
            {'name': 'test 1', 'description': 'test', 'level': '1', 'programming_language': 'Python'},
            {'name': 'test 2', 'description': 'test', 'level': '2', 'programming_language': 'JS'},
            {'name': 'test 3', 'description': 'test', 'level': '3', 'programming_language': 'Python'},
            {'name': 'test 4', 'description': 'test', 'level': '4', 'programming_language': 'C++'},
            {'name': 'test 5', 'description': 'test', 'level': '5', 'programming_language': 'C#'},
            {'name': 'test 6', 'description': 'test', 'level': '6', 'programming_language': 'Visual Basic'},
            {'name': 'test 7', 'description': 'test', 'level': '7', 'programming_language': 'SQL'},
            {'name': 'test 8', 'description': 'test', 'level': '8', 'programming_language': 'PHP'},
            {'name': 'test 9', 'description': 'test', 'level': '9', 'programming_language': 'Не выбрано'},
            {'name': 'test 10', 'description': 'test', 'level': '10', 'programming_language': 'Python'},
        ]

        for project in project_list:
            try:
                Project.objects.create(name=project['name'], description=project['description'], level=project['level'],
                                       programming_language=project['programming_language'])
                self.stdout.write(self.style.SUCCESS(f'Project \"{project["name"]}\" created successfully!'))
            except Exception as error:
                self.stdout.write(self.style.ERROR(f'Project \"{project["name"]}\" not created! \n Error: {error} \n {"-" * 5}'))

        for count in range(15):
            try:
                id_user=randint(User.objects.all()[1].pk, User.objects.last().pk)
                id_project = randint(Project.objects.first().pk, Project.objects.last().pk)
                user = User.objects.get(id=id_user)
                project = Project.objects.get(id=id_project)
                try:
                    UserProjectCompleted.objects.get(user_id=id_user, project_id=id_project)
                    self.stdout.write(self.style.ERROR(f'Сущность уже существует: {user.username} - {project.name}'))
                    continue
                except:
                    UserProjectCompleted.objects.create(user=user, project=project)
                    self.stdout.write(self.style.SUCCESS(f'Пользователь \"{user.username}\", выполнил проект \"{project.name}\"!'))
            except Exception as error:
                self.stdout.write(self.style.ERROR(f'Пользователь \"{user.username}\", не выполнил проект \"{project.name}\"! \n Error: {error} \n {"-" * 5}'))

