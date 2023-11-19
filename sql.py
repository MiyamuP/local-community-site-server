"""-- ユーザー一覧を表示
SELECT * FROM Users;

-- 投稿一覧を表示
SELECT * FROM Posts;

-- 特定のユーザーがした投稿を表示（例: UserIDが1のユーザーの投稿）
SELECT * FROM Posts WHERE UserID = 1;

-- ユーザーと投稿を結合して表示
SELECT Users.UserName, Posts.PostContent, Posts.PostDate
FROM Users
JOIN Posts ON Users.UserID = Posts.UserID;
"""


import sqlite3
#データベースの中身を見るときに使う
dbname = 'db.sqlite3'
conn = sqlite3.connect(dbname)
cur= conn.cursor()



sql = "SELECT * FROM memorymap_article;"
cur.execute(sql)
for c in cur:
    print(c)



# データベースへのコネクションを閉じる。(必須)
conn.close()

