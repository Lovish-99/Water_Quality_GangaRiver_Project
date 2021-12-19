from django.db import models

# Create your models here.
class insertddl(models.Model):
    pname = models.CharField(max_length=300)
    yesno = models.CharField(max_length=300)
    class Meta:
        db_table = "insertddl"

class Test(models.Model):
    name = models.CharField(max_length=4)

class insertgraph(models.Model):
    serv1 = models.CharField(max_length=300)

class insertgraph2(models.Model):
    service1 = models.CharField(max_length=300)
    service2 = models.CharField(max_length=300)
    service3 = models.CharField(max_length=300)
    class Meta:
        db_table = "insertgraph2"