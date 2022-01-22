from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from users.models import User


class Project(models.Model):
    '''
    Модель продуктов
    '''
    NO = 'Не выбрано'
    PYTHON = 'Python'
    JS = 'JS'
    C = 'C'
    C__ = 'C++'
    C_ = 'C#'
    VISUAL_BASIC = 'Visual Basic'
    SQL = 'SQL'
    PHP = 'PHP'

    LANGUAGE_CHOICES = (
        (NO, 'Не выбрано'),
        (PYTHON, 'Python'),
        (JS, 'JS'),
        (C__, 'C++'),
        (C_, 'C#'),
        (VISUAL_BASIC, 'Visual Basic'),
        (SQL, 'SQL'),
        (PHP, 'PHP'),
    )

    name = models.CharField(max_length=200, name='name')
    description = models.TextField(null=False, blank=False, name='description')
    level = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1),
                                                               MaxValueValidator(10)])
    programming_language = models.CharField(choices=LANGUAGE_CHOICES, verbose_name='programming_language',
                                            max_length=50, default=NO)
    check = models.BooleanField(default=False, name='check')
    date_created = models.DateTimeField(auto_now_add=True)
    id_telegram = models.CharField(max_length=15,verbose_name='ID_Телеграм', null=True, blank=True)
    username = models.CharField(max_length=30, verbose_name='Имя Телеграм', null=True, blank=True)
    is_active = models.BooleanField(default=True, name='is_active')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self) -> str:
        return f'Project {self.name} от {self.date_created}'


class UserProjectCompleted(models.Model):
    '''
    Модель пользователей выполнившие проекты
    '''


class UserProjectCompleted(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, name='user')
    project = models.ForeignKey(Project, on_delete=models.PROTECT, name='project')

    class Meta:
        verbose_name = 'Пользователь выполнивший проект'
        verbose_name_plural = "Пользователи выполнившие проект"

    def __str__(self) -> str:
        return f'Пользователь {self.user.username} выполнил проект {self.project.name}'

    def get_users_completed_project(self, project_id) -> set:
        return UserProjectCompleted.objects.all().filter(project_id=project_id)

    def get_projects_completed_user(self, user_id) -> set:
        return UserProjectCompleted.objects.all().filter(user_id=user_id)
