from django.db import models

# Create your models here.
class Aticle(models.Model):
	title=models.CharField(max_length=32,default='Title')
	content=models.TextField(null=True)
	pub_time=models.DateTimeField(null=True)
	#后台文章列表显示名称
	def __str__(self):
		return self.title

