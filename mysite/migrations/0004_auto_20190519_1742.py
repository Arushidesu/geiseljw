# Generated by Django 2.2.1 on 2019-05-19 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_auto_20190519_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campo',
            name='dia',
            field=models.CharField(choices=[('0', 'Domingo'), ('1', 'Segunda'), ('2', 'Terça'), ('3', 'Quarta'), ('4', 'Quinta'), ('5', 'Sexta'), ('6', 'Sábado')], max_length=1),
        ),
    ]