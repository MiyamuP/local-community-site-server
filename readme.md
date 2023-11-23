# これは何？
チームハッカソンで開発した「地域のイベントを共有できるコミュニティサイト
」のAPIサーバーとして稼働しているバックエンド
# 注意点
過去のプロダクトからコードを流用しているので、使っていないコードがある程度ある
# 使用技術
- django
- python
- django rest framework
- sqlite3
- (シェルスクリプト？)
# clone、zipでダウンロードした際の起動方法
ターミナルのいる位置がこのファイルと同じ階層のときに、
```
bash init.sh
```
と打つことで、シェルスクリプトが走り、初期化される。
またmigrationやdb.sqliteを削除した場合は、

```
python manage.py create_prefecture
```
と打つことで、都道府県データを3都道府県分一括で登録できる自作シェルスクリプトが走る(init.shにコマンドとして含まれています)

# DB
テーブル構造（実装した形）
# 地域テーブル(３番優先）Prefecture
- 都道府県ID[“Prefecture_id”]
- 記事ID[“Article_id”]
- 緯度[“lat”]
- 経度[“lon”]

# 記事テーブル(１番優先)article
テキスト[“text”]
記事タイトル[“Article_title”]
記事ID[“Article_id”]
作成者[“Author”]
作成日時[“create_time”]
地域への外部キー[“Prefecture_id”]

# コメントテーブル(2番優先）comment
- 記事への外部キー[“Parent_Article_id”]
- id[“Comment_id”]
- 本文["text"]
- ユーザーへの外部キー[“Author_id”]
- 投稿者名["author_name"]
- 投稿日時["create_time"]
- 親コメントへのリンク["parent_comment_id"]
    - 実装が歪になったので、時間があれば修正推奨
# APIの機能一覧
## post
- 都道府県を指定して、記事を投稿
- 記事を指定して、コメントを投稿
- 都道府県を追加
## get
- 登録している都道府県をすべて取得する
- 都道府県を指定し、紐づいている記事をすべて取得
- 指定したIDの記事を返す
- 記事に紐づいている親コメントをすべて取得
- 親コメントに紐づいている子供コメントをすべて取得





