from django.db import models

# Create your models here.
class user(models.Model):
    cookie = models.CharField(max_length=1000)
    id=models.AutoField(primary_key=True)
    start_time=models.DateTimeField(auto_now=True)
    end_time=models.DateTimeField(auto_now=True)
    password=models.CharField(max_length=1000)
    name=models.CharField(max_length=1000)
    email=models.CharField(max_length=1000)
    superuser=models.CharField(max_length=1000,default="普通用户")
    # money_left=models.CharField(max_length=1000)
    # 余额数
    money_left=models.FloatField(default=5.0)
    #只记录三次聊天记录
    def __str__(self):
        return self.name
class chat_history(models.Model):
    id=models.AutoField(primary_key=True)
    generar_time=models.DateTimeField(auto_now=True)
    user_id=models.ForeignKey(user,on_delete=models.CASCADE)#外键#on_delete=models.CASCADE#级联删除
    content1=models.CharField(max_length=1500,default="")
    content2=models.CharField(max_length=1500,default="")
    content3=models.CharField(max_length=1500,default="")
    timeofcontent1=models.DateTimeField(auto_now=True)
    timeofcontent2=models.DateTimeField(auto_now=True)
    timeofcontent3=models.DateTimeField(auto_now=True)
    # 只记录三次聊天记录

    def __str__(self):
        return self.id