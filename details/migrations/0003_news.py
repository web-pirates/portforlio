# Generated by Django 3.0.8 on 2020-07-31 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0002_inquery_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EMAIL', models.EmailField(max_length=200)),
            ],
        ),
    ]
