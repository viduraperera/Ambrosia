# Generated by Django 3.1.1 on 2020-09-07 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ambrosia_Project', '0002_leafinventory'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeaGrades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teaGrade', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'tea_grade',
            },
        ),
    ]