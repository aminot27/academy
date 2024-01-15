from django.db import models
from master_serv.models.base_model import BaseModel

class Parent(BaseModel):
    parent_id = models.AutoField(verbose_name='ID', primary_key=True)
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, verbose_name='User')
    phone = models.CharField(verbose_name='Phone', max_length=20)
    email = models.EmailField(verbose_name='Email')

    class Meta:
        db_table = 'academy_parent'
        ordering = ['parent_id']
        verbose_name = 'Parent'
        verbose_name_plural = 'Parents'

    def __str__(self):
        return self.user.get_full_name()