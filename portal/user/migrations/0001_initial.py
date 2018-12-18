# Generated by Django 2.1.4 on 2018-12-16 05:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('repo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.SlugField(blank=True, help_text='slug', unique=True)),
                ('name', models.CharField(blank=True, max_length=60, null=True)),
                ('avatar', models.CharField(blank=True, max_length=30, null=True)),
                ('token', models.CharField(blank=True, max_length=100, null=True)),
                ('daysCount', models.IntegerField(blank=True, null=True)),
                ('prCount', models.IntegerField(blank=True, null=True)),
                ('issueCount', models.IntegerField(blank=True, null=True)),
                ('repoOwnCount', models.IntegerField(blank=True, null=True)),
                ('points', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('basePoints', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('contributionPoints', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('activityPoints', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('creationPoints', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('communityPoints', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('skill', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Profile')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repo.Topic', verbose_name='Topic Name')),
            ],
        ),
        migrations.CreateModel(
            name='UserTopics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='topics',
            field=models.ManyToManyField(related_name='user_topics', through='user.UserTopic', to='repo.Topic'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]