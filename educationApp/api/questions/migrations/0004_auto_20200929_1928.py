# Generated by Django 3.1.1 on 2020-09-29 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20200927_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='equation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='equations_answere',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='optionA',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='optionB',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='optionC',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='optionD',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
