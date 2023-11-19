バックエンドAPI仕様書
使用方法の想定として、１つのpcでReactとDjangoをポート違いで立ち上げて、ReactからDjangoのAPIを叩くのを想定している
# articlelist/<都道府県ID>
概要
都道府県IDに紐づいた記事の一覧を配列形式で返します

path説明
http://127.0.0.1:8000/api/articlelist/都道府県ID/
返ってくるもの：都道府県IDに紐づいた全投稿

```
GET /api/articlelist/1/
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "text": "test",
        "title": "test",
        "create_time": "2023-11-19T09:13:33.397697+09:00",
        "prefecture_id": 1,
        "author": "test",
        "prefecture_name": "北海道"
    },
    {
        "text": "test1",
        "title": "test2",
        "create_time": "2023-11-19T09:13:55.933368+09:00",
        "prefecture_id": 1,
        "author": "test3",
        "prefecture_name": "北海道"
    }
]

```


実際のpath例
http://127.0.0.1:8000/api/articlelist/1/
# 'article/'
概要
POSTで記事を投稿します

path説明
http://127.0.0.1:8000/api/article
効果：新規の記事を作成

POSTするもの

Key
Value
text
記事の内容(String)
title
タイトル(String)
author
執筆者名(String)
prefecture_id
1-47の都道府県コード(Integer)


POST
{
    "text": "記事の内容",
    "title": "タイトル",
    "author": "投稿者名",
    "prefecture_id": 1
}

```
POST /api/article/
HTTP 201 Created
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "article_id": "72445533-2058-42d0-adc9-be20ebc828af",
    "text": "test",
    "title": "test",
    "author": "test",
    "create_time": "2023-11-19T09:31:42.250635+09:00",
    "prefecture_id": 1
}
```
# 'article/<article_id>/'

概要
指定したarticle_idの記事を返します
path 例
http://127.0.0.1:8000/api/article/1




```
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "article_id": "fc7eb719-8c6e-4ed9-9bfd-714f9f1f58bc",
    "text": "hoge",
    "title": "hoge",
    "author": "hoge",
    "create_time": "2023-11-19T09:33:07.036236+09:00",
    "prefecture_id": 1
}
```

# 'prefecture/'
概要
都道府県をPOSTで追加します(デバッグ用途を現時点では想定)
http://127.0.0.1:8000/api/prefecture/





Key
Value
prefecture_id
都道府県コード(String)
prefecture_name
都道府県名(String)


```
POST /api/prefecture/
HTTP 201 Created
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 48,
    "prefecture_id": "48",
    "prefecture_name": "北方領土"
}
```

# コメントを投稿
http://127.0.0.1:8000/api/comment_post/

POST /api/comment_post/
author_nameは自動でしてされないので、”名無し”などとフロント側で入れてほしい
	ログインが実装できたら、ユーザー名を入れる
```
HTTP 201 Created
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "comment_id": "b3dcac5d-ae3d-4f85-9275-32476de95bd1",
    "text": "テスト２",
    "author_name": "７７４",
    "create_time": "2023-11-19T10:52:46.405337+09:00",
    "article_id": "c50861b0-6886-4abe-bc8a-31b59288148d"

}
```

# 記事に紐づいたとコメントを取得(親コメントのみ)
path:
http://127.0.0.1:8000/api/commentlist/記事ID


例：
http://127.0.0.1:8000/api/commentlist/c50861b0-6886-4abe-bc8a-31b59288148d


GET /api/commentlist/c50861b0-6886-4abe-bc8a-31b59288148d



```

HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "text": "テスト２",
        "create_time": "2023-11-19T10:52:34.482891+09:00",
        "comment_id": "6be5cbbb-b778-49b1-b8c2-b667691988fb",
        "au": "",
        "article_id": "c50861b0-6886-4abe-bc8a-31b59288148d"
    },
    {
        "text": "テスト２",
        "create_time": "2023-11-19T10:52:46.405337+09:00",
        "comment_id": "b3dcac5d-ae3d-4f85-9275-32476de95bd1",
        "author_name": "７７４",
        "article_id": "c50861b0-6886-4abe-bc8a-31b59288148d"
 
}

```



# 親コメントを指定して、子供コメントを表示
http://127.0.0.1:8000/api/comment_child/05f241db-66a0-4f04-ba64-f8bc939adb6d
概要：http://127.0.0.1:8000/api/comment_child/親コメントid
/api/comment_child/05f241db-66a0-4f04-ba64-f8bc939adb6d
```
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "comment_id": "7ac76d2b-f99e-4566-99b4-221b27168b1c",
        "text": "kome2",
        "author_name": "774",
        "create_time": "2023-11-19T13:28:07.172634+09:00",
        "parent_comment_id": "05f241db-66a0-4f04-ba64-f8bc939adb6d",
        "article_id": "4f79779c-4cbb-4a5d-92b2-9a89dc0e0e79"
    }
]
```

# 都道府県情報一覧を取得
都道府県id, 都道府県名,緯度，経度を取得します
path:
http://127.0.0.1:8000/api/prefecturelist


例：
http://127.0.0.1:8000/api/prefecturelist


GET /api/prefecturelist

```
GET /api/prefecturelist/
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "prefecture_id": "1",
        "prefecture_name": "北海道",
        "lat": 43.06417,
        "lon": 141.34694
    },
    {
        "id": 2,
        "prefecture_id": "13",
        "prefecture_name": "東京",
        "lat": 35.6895,
        "lon": 139.6917
    },
    {
        "id": 3,
        "prefecture_id": "27",
        "prefecture_name": "大阪",
        "lat": 34.6937,
        "lon": 135.5023
    }
]
```
