# Generated by Django 4.2.4 on 2023-08-24 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.topic'),
        ),
    ]
