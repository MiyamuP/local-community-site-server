from django.urls import path
from .views import EventLocationView#親と子
from .views import EventListAPIView#10件

from .views import EventCreateView#空のイベント
from .views import LocationCreateAPIView,ArticleCreateAPIView,ArticleView, ArticleListCreateAPIView,ArticleListView,ComentCreateAPIView,CommentListView, PrefectureListView,CommentChildListView

from .views import GetCsrf,LoginView
urlpatterns = [
    
    path('events/',EventListAPIView.as_view()),#10件
    path('event/<uuid:uuid>/', EventLocationView.as_view(), name='event-location'),#詳細
    path('event/',EventCreateView.as_view()),#空のイベント
    path('location/<uuid:uuid>/', LocationCreateAPIView.as_view()), # イベントにロケーション情報をPOSTする
    path('auth/login/', LoginView.as_view()), # ログイン周り
    path('csrf/', GetCsrf.as_view(), name="csrf"),

    path('article/', ArticleCreateAPIView.as_view()),#post
    path('article/<article_id>/', ArticleView.as_view(), name='article-view'),#詳細

    path('prefecture/', ArticleListCreateAPIView.as_view()),#都道府県を登録
    path('articlelist/<prefecture_id>/', ArticleListView.as_view(), name='article-list-view'),#詳細
    path('comment_post/',ComentCreateAPIView.as_view()),
    path('commentlist/<article_id>',CommentListView.as_view(),name='commetn-list-view'),
    path('prefecturelist/', PrefectureListView.as_view()),#都道府県をすべて取得
    path('comment_child/<parent_id>',CommentChildListView.as_view()),
]