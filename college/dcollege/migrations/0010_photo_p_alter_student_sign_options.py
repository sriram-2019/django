# Generated by Django 4.1.5 on 2023-03-20 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dcollege', '0009_alter_staff_sign_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='photo_p',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(db_column='file_name', max_length=264)),
                ('file', models.BinaryField(db_column='file_data')),
            ],
            options={
                'db_table': 'pdf_files',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='student_sign',
            options={'managed': True},
        ),
    ]
