# Generated by Django 5.0.3 on 2024-05-14 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cogn', '0007_rename_sluh_pam_student_rawen1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='rawen1',
            new_name='rawen',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='sluh_pam1',
            new_name='sluh_pam',
        ),
    ]
