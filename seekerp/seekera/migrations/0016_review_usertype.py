# Generated by Django 4.2 on 2023-04-16 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seekera', '0015_alter_review_provider'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='usertype',
            field=models.CharField(default='Unknown', max_length=20),
        ),
    ]