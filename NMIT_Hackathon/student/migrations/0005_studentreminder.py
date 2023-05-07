# Generated by Django 4.1.3 on 2023-05-06 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_remove_studenthomework_id_studenthomework_hw_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentReminder',
            fields=[
                ('rmdr_id', models.AutoField(primary_key=True, serialize=False)),
                ('rmdr_title', models.CharField(max_length=50)),
                ('rmdr_desc', models.CharField(max_length=500)),
                ('rmdr_author', models.CharField(max_length=50)),
                ('std_reg_no', models.CharField(max_length=50)),
                ('hw_date', models.DateField(auto_now=True)),
            ],
        ),
    ]
