from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
	#用户学习的主题
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User)
	def __str__(self):
		#返回模型的字符串表示
		return self.text

#主题下的条目，一对多关系
class Entry(models.Model):
	topic = models.ForeignKey(Topic)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	#存储用于管理模型的额外信息
	class Meta():
		verbose_name_plural = 'entries'

	def __str__(self):
		return self.text[:50] + "..."

			