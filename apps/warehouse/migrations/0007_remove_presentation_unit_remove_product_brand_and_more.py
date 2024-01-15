# Generated by Django 4.0 on 2024-01-15 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0006_productdetail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presentation',
            name='unit',
        ),
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='productdetail',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productinput',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productoutput',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productpresentation',
            name='presentation',
        ),
        migrations.RemoveField(
            model_name='productpresentation',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productsubcategory',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productsubcategory',
            name='subcategory',
        ),
        migrations.RemoveField(
            model_name='specification',
            name='product',
        ),
        migrations.RemoveField(
            model_name='specificationdetail',
            name='specification',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Presentation',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ProductDetail',
        ),
        migrations.DeleteModel(
            name='ProductInput',
        ),
        migrations.DeleteModel(
            name='ProductOutput',
        ),
        migrations.DeleteModel(
            name='ProductPresentation',
        ),
        migrations.DeleteModel(
            name='ProductSubcategory',
        ),
        migrations.DeleteModel(
            name='Specification',
        ),
        migrations.DeleteModel(
            name='SpecificationDetail',
        ),
        migrations.DeleteModel(
            name='Subcategory',
        ),
        migrations.DeleteModel(
            name='Unit',
        ),
    ]
