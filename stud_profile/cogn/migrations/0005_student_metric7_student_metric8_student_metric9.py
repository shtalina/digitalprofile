# Generated by Django 5.0.3 on 2024-05-12 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cogn', '0004_student_gruppa1'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='metric7',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='metric8',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='metric9',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
