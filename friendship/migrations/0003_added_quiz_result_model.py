# Generated by Django 2.2 on 2019-04-04 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('friendship', '0002_auto_20190404_0850'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizResults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='friendship.Answer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='friendship.Question')),
                ('quiz_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_result', to='friendship.QuizDetails')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
