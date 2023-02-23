from django.db import models

# Create your models here.
class Usagedb(models.Model): # DataTable
    send_time=models.CharField(max_length=32,default='00:00:00')
    now_time2=models.DateTimeField(auto_now=True)
    cpu_ratio=models.FloatField(default='none')#max_digits = 10,decimal_places = 2)
    memory_ratio=models.FloatField(default='none')#max_digits = 10,decimal_places = 2)