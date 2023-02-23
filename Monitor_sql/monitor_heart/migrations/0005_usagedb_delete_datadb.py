# Generated by Django 4.1.6 on 2023-02-19 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor_heart', '0004_auto_20230213_2056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usagedb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_time', models.CharField(default='00:00:00', max_length=32)),
                ('now_time2', models.DateTimeField(auto_now=True)),
                ('cpu_ratio', models.FloatField(default='none')),
                ('memory_ratio', models.FloatField(default='none')),
            ],
        ),
        migrations.DeleteModel(
            name='Datadb',
        ),
    ]