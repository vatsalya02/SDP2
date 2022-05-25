# Generated by Django 3.2.3 on 2021-05-16 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DreamDine', '0002_bill'),
    ]

    operations = [
        migrations.CreateModel(
            name='book_tables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=60)),
                ('phone', models.IntegerField()),
                ('guest', models.IntegerField()),
                ('date_table', models.DateField(max_length=50)),
                ('time_table', models.TimeField(max_length=60)),
                ('category', models.CharField(max_length=50)),
                ('msg', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'book_tables',
            },
        ),
    ]