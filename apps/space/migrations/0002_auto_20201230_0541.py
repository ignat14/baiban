# Generated by Django 3.1.4 on 2020-12-30 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='folder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='space.folder'),
        ),
    ]
