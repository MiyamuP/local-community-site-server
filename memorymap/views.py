from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Event, Location,Comment

from django.shortcuts import render#不明
from rest_framework.generics import ListAPIView#直近10件
from .serializers import EventSerializer#10件
from .serializers import EventDSerializer#詳細
from .serializers import EventCSerializer#空のイベントを作成
from rest_framework.generics import RetrieveAPIView#投稿の詳細
from rest_framework.generics import CreateAPIView#空のイベントを作成
from .serializers import EventSerializer, UserSerializer, LocationSerializer, ArticleSerializer, PrefectureListSerializer,CommentSerializer
from django.contrib.auth import authenticate, login#ruki
from .models import Event, Location, User, Article, Prefecture
from rest_framework import authentication, exceptions#ruki
from django.middleware.csrf import get_token


class EventListAPIView(ListAPIView):#投稿10件取得
    queryset = Event.objects.all().order_by('-hold_date')[:10]
    serializer_class = EventSerializer

# イベントにロケーション情報をPOSTする(URLに記載されたuuidはそのままEventフィールドに適応される)
class LocationCreateAPIView(CreateAPIView):
    serializer_class = LocationSerializer

    def perform_create(self, serializer):
        event_uuid = self.kwargs.get('uuid')
        event = Event.objects.get(uuid=event_uuid)
        serializer.save(event=event)

# ログイン周り
class LoginView(APIView):
    serializer_class = UserSerializer


class EventLocationView(APIView):#投稿詳細
    def get(self, request, uuid):
        event = get_object_or_404(Event, uuid=uuid)
        locations = Location.objects.filter(event=event)
        serializer = EventDSerializer(event)
        data = serializer.data
        data["locations"] = [{
            "title": location.title,
            "lat": location.lat,
            "lon": location.lon
        } for location in locations]
        return Response(data)






class EventCreateView(CreateAPIView):#空のイベント作成
    queryset = Event.objects.all()
    serializer_class = EventCSerializer

def post(self, request):#ruki
    user = authenticate(request, username=request.data['username'], password=request.data['password'])
    if user:
        login(request, user)
        return Response({})
    else:
        raise exceptions.AuthenticationFailed('アカウントが見つかりませんでした')
    

class GetCsrf(APIView):
    def get(self, request):
        return Response({'csrftoken':get_token(request)}, status=200)
    

# class ArticleCreateAPIView(CreateAPIView):
#     serializer_class = ArticleSerializer

#     def perform_create(self, serializer):
#         article_id = self.kwargs.get('article_id')
#         event = Event.objects.get(uuid = article_id)
#         serializer.save(event=event)

class ArticleCreateAPIView(CreateAPIView):#空のaricle
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleView(APIView):#投稿詳細
    def get(self, request, article_id):
        print("articleid",article_id)
        article = get_object_or_404(Article, article_id=article_id)
        
        # article = Article.objects.filter(article=article)
        serializer = ArticleSerializer(article)
        data = serializer.data

        # data["locations"] = [{
        #     "title": art.title,
            
        # } for art in article]
        return Response(data)
    
class ArticleListCreateAPIView(CreateAPIView):#空のaricle
    queryset = Article.objects.all()
    serializer_class = PrefectureListSerializer

class ArticleListView(APIView):#都道府県に結びついた投稿をたくさん取得
    def get(self, request, prefecture_id):
        # print("articleid",article_id)
        
        prefecture = get_object_or_404(Prefecture,prefecture_id=prefecture_id)
        articles = get_list_or_404(Article,prefecture_id=prefecture_id)
        articles = Article.objects.filter(prefecture_id = prefecture_id)#都道府県
        # articles = Article.objects.filter(prefecture_id=prefecture)

        pre_serializer = PrefectureListSerializer(prefecture)
        pre_data = pre_serializer.data

        serializer = ArticleSerializer(articles, many=True)
        data = serializer.data

        # for i in data:
        #     print(i)

        d = [{
            "text":ar["text"],
            "title":ar["title"],
            "create_time":ar["create_time"],
            "prefecture_id":ar["prefecture_id"],
            "author":ar["author"],
            "prefecture_name":pre_data["prefecture_name"],
            "article_id":ar["article_id"]
        } for ar in data]
        
        return Response(d)
    
class ComentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentListView(APIView):#記事に結びついたコメントをすべて取得
    def get(self, request, article_id):
        # print("articleid",article_id)
        
        # prefecture = get_object_or_404(Prefecture,prefecture_id=prefecture_id)
        article = get_object_or_404(Article,article_id=article_id)
        # articles = get_list_or_404(Article,prefecture_id=prefecture_id)
        comments = get_list_or_404(Comment,article_id=article_id)#確認
        comments = Comment.objects.filter(article_id = article_id)#都道府県
        parents_comments =  Comment.objects.filter(article_id = article_id,parent_comment_id = '')#
        # pre_serializer = PrefectureListSerializer(comments)
        # pre_data = pre_serializer.data

        serializer = CommentSerializer(parents_comments, many=True)
        data = serializer.data
        # child_comments = Comment.objects.filter(parent_comment_id = '')
        child_comments = []
        parents_comments = []#親コメントのみ
        for i in comments:
            if(i.parent_comment_id != ''):
                child_comments.append(i.parent_comment_id)
            else:
                parents_comments.append(i)
        print("-------")
        print(list(child_comments))#親を持っているコメント

        print(parents_comments)
        # for i in data:
        #     print(i)
        
        d = [{
            "text":ar["text"],
            
            "create_time":ar["create_time"],
            "comment_id":ar["comment_id"],
            "parent_comment_id":ar["parent_comment_id"],
            "author_name":ar["author_name"],
            "article_id":ar["article_id"],
            "has_replay":ar['comment_id'] in child_comments
        } for ar in data]
        
        return Response(d)
    
class PrefectureListView(APIView):
    def get(self, request):
        # articles = Article.objects.filter(prefecture_id = prefecture_id)#都道府県
        prefecture = Prefecture.objects.all()
        

        # pre_serializer = PrefectureListSerializer(comments)
        # pre_data = pre_serializer.data

        serializer = PrefectureListSerializer(prefecture, many=True)
        data = serializer.data

        # for i in data:
        #     print(i)

        # d = [{
        #     "text":ar["text"],
            
        #     "create_time":ar["create_time"],
        #     "comment_id":ar["comment_id"],
            
        #     "author_name":ar["author_name"],
        #     "article_id":ar["article_id"]
        # } for ar in data]
        
        return Response(data)

class CommentChildListView(APIView):#親コメントのidを送れば、子供コメントをすべて表示
    def get(self, request,parent_id):
        childs = Comment.objects.filter(parent_comment_id = parent_id)
        serializer = CommentSerializer(childs, many=True)
        data = serializer.data
        return Response(data)
