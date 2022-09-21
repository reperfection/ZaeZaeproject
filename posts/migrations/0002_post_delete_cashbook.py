# Generated by Django 4.1.1 on 2022-09-21 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateTimeField(verbose_name='data published')),
                ('content', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Cashbook',
        ),
    ]
