# Generated by Django 3.2.16 on 2023-02-04 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datadb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('now_time', models.DateTimeField(auto_now_add=True)),
                ('cpu_ratio', models.FloatField()),
                ('memory_ratio', models.FloatField()),
            ],
        ),
    ]
