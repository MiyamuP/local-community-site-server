
from rest_framework import serializers

from .models import Event, Location, User, Article, Prefecture,Comment

class EventLSerializer(serializers.ModelSerializer):#投稿詳細
    class Meta:
        model = Location
        fields = ('title', 'lat', 'lon')


class EventDSerializer(serializers.ModelSerializer):#投稿詳細
    locations = EventLSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ('title', 'text', 'locations')



class EventSerializer(serializers.ModelSerializer):#投稿10件
    hold_date = serializers.DateTimeField(format="%m/%d %H:%M:%S", read_only=True)
    class Meta:
        model = Event
        
        fields = ('uuid','title','thumbnail','lat','lon','hold_date')
class EventCSerializer(serializers.ModelSerializer):#投稿空のイベント作成
    class Meta:
        model = Event
        fields = '__all__'
class LocationSerializer(serializers.ModelSerializer): # Location情報を取得
    class Meta:
        model = Location
        fields = '__all__'
        read_only_fields = ('uuid','event')

class ArticleSerializer(serializers.ModelSerializer): # Location情報を取得
    class Meta:
        model = Article
        fields = '__all__'
        # read_only_fields = ('article_id', 'create_time')

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255, style={'input_type': 'password'})

    class Meta:
        fields = ('username','password')


class PrefectureListSerializer(serializers.ModelSerializer): # article
    class Meta:
        model = Prefecture
        fields = '__all__'
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields='__all__'

