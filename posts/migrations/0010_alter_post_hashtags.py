# Generated by Django 4.0.6 on 2022-11-05 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_hashtag_post_hashtags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='hashtags',
            field=models.ManyToManyField(blank=True, related_name='hashtagged', to='posts.hashtag'),
        ),
    ]
