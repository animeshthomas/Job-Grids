# Generated by Django 4.2 on 2023-04-16 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seekera', '0014_review_provider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='provider',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='seekera.job_providers'),
        ),
    ]