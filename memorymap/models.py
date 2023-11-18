from django.db import models
from django.contrib.auth.models import AbstractUser

import uuid, os

# Create your models here.


class User(AbstractUser):
    def img_path(self, filename):
        result = 'profile/{}{}'.format(str(uuid.uuid4().hex), os.path.splitext(filename)[-1])
        return result
    
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, primary_key=True)
    prof_image = models.ImageField(upload_to=img_path ,null=True, blank=True)
    
class Event(models.Model):
    """みずがめ

    Args:
        thumbnail (ImageField): 作成したが、間違っている可能性あり
    """
    def img_path(self, filename):#Userと同じ
        result = 'event/{}{}'.format(str(uuid.uuid4().hex), os.path.splitext(filename)[-1])
        return result
    

    uuid = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, primary_key=True)
    title = models.CharField(max_length = 127)
    #text = models.CharField(_(""), max_length=50)
    text = models.CharField(max_length=511,blank=True)
    thumbnail = models.ImageField( upload_to=img_path, null = True,blank = True)
    create_at = models.DateTimeField( auto_now=False,auto_now_add=True)#insertされた時だけ日付変わる
    hold_date = models.DateTimeField( auto_now=False, auto_now_add=False)#insertされた時だけ日付変わる
    edited_at = models.DateTimeField( auto_now=True, auto_now_add=False)#save()などで更新されたときに日付変わる

    lat = models.FloatField((""))#FloatFieldは2進数で小数を表す
    lon = models.FloatField((""))#FloatFieldは2進数で小数を表す
    member = models.ManyToManyField(User, blank = True,related_name = 'events')
    

class Location(models.Model):
    """Ruki
    """
    def img_path(self, filename): # Userと同じ
        result = 'location/{}{}'.format(str(uuid.uuid4().hex), os.path.splitext(filename)[-1])
        return result

    uuid = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, primary_key=True)
    title = models.CharField( max_length = 127) # 場所の名称
    event = models.ForeignKey( Event, on_delete=models.CASCADE) # 外部キー(Eventと1対多)
    photo = models.ImageField( upload_to=img_path, null = True, blank = True)
    address = models.CharField( max_length = 127, null = True, blank = True) # 住所
    create_at = models.DateTimeField( auto_now=False, auto_now_add=True) #DBにinsertされた時だけ日付変わる
    hold_date = models.DateTimeField( auto_now=False, auto_now_add=False) #DBにinsertされた時だけ日付変わる

    lat = models.FloatField(("")) # FloatFieldは2進数で小数を表す
    lon = models.FloatField(("")) # FloatFieldは2進数で小数を表す



class Prefecture(models.Model):
    # def img_path(self, filename): # Userと同じ
    #     result = 'location/{}{}'.format(str(uuid.uuid4().hex), os.path.splitext(filename)[-1])
    #     return result
    # prefecture_id = models.

    prefecture_id = models.CharField(max_length=50)
    # municipality_id = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, primary_key=True)
    prefecture_name = models.CharField( max_length = 127, null = True, blank = True)
    # municipality_name = models.CharField( max_length = 127, null = True, blank = True)
    

class Article(models.Model):
    """Ruki
    """
    # def img_path(self, filename): # Userと同じ
    #     result = 'location/{}{}'.format(str(uuid.uuid4().hex), os.path.splitext(filename)[-1])
    #     return result
    text = models.CharField( max_length = 256, null = True, blank = True) # テキスト
    title = models.CharField( max_length = 256, null = True, blank = True) # タイトル
    article_id = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, primary_key=True)
    author = models.CharField( max_length = 256, null = True, blank = True) # ユーザー
    # likes
    create_time = models.DateTimeField( auto_now=False, auto_now_add=True) #DBにinsertされた時だけ日付変わる
    # comment_id = models.CharField( max_length = 256, null = True, blank = True) # コメントID
    prefecture_id = models.ForeignKey(Prefecture,on_delete=models.CASCADE)
    # prefecture_id = models.CharField(max_length=50)


    # event = models.ForeignKey( Event, on_delete=models.CASCADE) # 外部キー(Eventと1対多)
    # photo = models.ImageField( upload_to=img_path, null = True, blank = True)
    # address = models.CharField( max_length = 127, null = True, blank = True) # 住所
    # create_at = models.DateTimeField( auto_now=False, auto_now_add=True) #DBにinsertされた時だけ日付変わる
    # hold_date = models.DateTimeField( auto_now=False, auto_now_add=False) #DBにinsertされた時だけ日付変わる

    # lat = models.FloatField(("")) # FloatFieldは2進数で小数を表す
    # lon = models.FloatField(("")) # FloatFieldは2進数で小数を表す



    # coordinate = 
    