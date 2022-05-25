# Generated by Django 3.2.3 on 2021-05-16 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DreamDine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=60)),
                ('address', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('zip', models.IntegerField()),
                ('name_on_card', models.CharField(max_length=50)),
                ('cardno', models.IntegerField()),
                ('expmonth', models.IntegerField()),
                ('expyear', models.IntegerField()),
                ('cvv', models.IntegerField()),
            ],
            options={
                'db_table': 'bill',
            },
        ),
    ]