from django.db import models
from master_serv.models.base_model import BaseModel

class Student(BaseModel):
    student_id = models.AutoField(verbose_name='ID', primary_key=True)
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, verbose_name='User')
    registration_number = models.CharField(verbose_name='Registration Number', max_length=50, unique=True)

    class Meta:
        db_table = 'academy_student'
        ordering = ['student_id']
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return self.user.get_full_name()