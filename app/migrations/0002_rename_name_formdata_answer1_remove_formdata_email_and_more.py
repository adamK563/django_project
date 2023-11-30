# Generated by Django 4.2.7 on 2023-11-27 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formdata',
            old_name='name',
            new_name='answer1',
        ),
        migrations.RemoveField(
            model_name='formdata',
            name='email',
        ),
        migrations.RemoveField(
            model_name='formdata',
            name='message',
        ),
        migrations.AddField(
            model_name='formdata',
            name='answer2',
            field=models.CharField(default='Default Answer', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formdata',
            name='answer3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='formdata',
            name='answer4',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='formdata',
            name='answer5',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='formdata',
            name='question',
            field=models.CharField(default='Default Answer', max_length=100),
            preserve_default=False,
        ),
    ]