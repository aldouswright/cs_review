from django.db import models

# Create your models here.
class Page(models.Model):
	pid = models.AutoField(primary_key=True)
	uid = models.ForeignKey("User", on_delete=models.CASCADE)
	title = models.CharField(null=False, max_length=150)
	contents = models.TextField()
	count = models.BigIntegerField(default=0)


class User(models.Model):
	uid = models.AutoField(primary_key=True)
	email = models.EmailField(null=False)
	password = models.CharField(null=False, max_length=100)