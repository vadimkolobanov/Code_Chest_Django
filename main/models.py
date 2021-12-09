from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# from auth.models import User


class Project(models.Model):
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
    is_active = models.BooleanField(default=True, name='is_active')

    def __str__(self) -> str:
        return f'Project {self.name} от {self.date_created}'

#
# class UserProjectCompleted(models.Model):
#     user = models.ForeignKey(User, on_delete=models.PROTECT, name='user')
#     project = models.ForeignKey(Project, on_delete=models.PROTECT, name='project')
#
#     def __str__(self) -> str:
#         return f'{self.user} completed {self.project}'
#
#     def get_users_copleted_project(self, project_id) -> set:
#         return UserProjectCompleted.objects.all().filter(project_id=project_id)
#
#     def get_projects_completed_user(self, user_id) -> set:
#         return UserProjectCompleted.objects.all().filter(user_id=user_id)

