# インストール&起動

```
bash init.sh
```

# migrationやdb.sqliteを削除した場合
以下のコマンドで都道府県データを自動登録できます(init.shにコマンドとして含まれています)

```
python manage.py create_prefecture
```