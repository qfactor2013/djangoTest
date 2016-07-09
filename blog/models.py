from django.db import models #db에 있는 models을 가져옴
from django.utils import timezone # 유틸에 있는 timezone을 가져옴
# Create your models here.

class Post(models.Model):
#Post라는 객체를 정의함 인수로 장고모델을 가져왔음
#장고모델이기 때문에 데이터베이스에 저장된다.
	author = models.ForeignKey('auth.User') #외래키, 다른 객체에 대한 링크
	title  = models.CharField(max_length=200) #글자수 제한 
	text   = models.TextField(); # 글자수제한없음
	created_date	=	models.DateTimeField(default=timezone.now) #Date형식
	published_date	=	models.DateTimeField(blank=True, null=True)

	def publish(self): #파이썬의 메소드
		self.published_date = timezone.now()
		self.save()


	def __str__(self):
			return self.title