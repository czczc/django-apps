# Generated by Django 3.1.7 on 2021-03-25 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0002_auto_20210325_0101'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-year', '-arXiv']},
        ),
        migrations.AlterField(
            model_name='article',
            name='arXiv',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='doi',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
