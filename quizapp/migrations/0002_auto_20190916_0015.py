# Generated by Django 2.2.3 on 2019-09-15 18:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quizapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='max_score',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='time_lim',
            field=models.PositiveIntegerField(help_text='Time Limit should be in MINUTES.'),
        ),
        migrations.CreateModel(
            name='UserQuizResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveIntegerField()),
                ('max_score', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_max_score', to='quizapp.Quiz')),
                ('quiz_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_title', to='quizapp.Quiz')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
