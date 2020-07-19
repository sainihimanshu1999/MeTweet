# Generated by Django 2.1.5 on 2020-07-19 08:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0006_auto_20200719_1401'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweetlike',
            name='tweet',
        ),
        migrations.RemoveField(
            model_name='tweetlike',
            name='user',
        ),
        migrations.AlterField(
            model_name='tweet',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='tweet_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='TweetLike',
        ),
    ]