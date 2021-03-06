# Generated by Django 3.2.3 on 2021-05-17 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DreamDine', '0003_book_tables'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=50)),
                ('dcategory', models.CharField(max_length=50)),
                ('dcapacity', models.IntegerField()),
                ('dicategory', models.CharField(max_length=50)),
                ('dicapacity', models.IntegerField()),
                ('tcategory', models.CharField(max_length=50)),
                ('tcapacity', models.IntegerField()),
                ('pcategory', models.CharField(max_length=50)),
                ('pcapacity', models.IntegerField()),
                ('rcategory', models.CharField(max_length=50)),
                ('rcapacity', models.IntegerField()),
                ('decategory', models.CharField(max_length=50)),
                ('decapacity', models.IntegerField()),
                ('drcategory', models.CharField(max_length=50)),
                ('drcapacity', models.IntegerField()),
                ('maincategory', models.CharField(max_length=50)),
                ('maincapacity', models.IntegerField()),
            ],
            options={
                'db_table': 'Catering',
            },
        ),
    ]
