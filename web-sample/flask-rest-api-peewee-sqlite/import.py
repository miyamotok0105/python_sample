# -*- coding: utf-8 -*-
import peewee

# データベースを指定
db = peewee.SqliteDatabase("data.db")

# ユーザーモデルを定義
class User(peewee.Model):
    userId = peewee.TextField()
    userCompany = peewee.TextField()
    userDiscountRate = peewee.IntegerField()

    class Meta:
        database = db

# ユーザーテーブル作成
User.create_table()

# tsvファイルを一行ずつ読み込んでタブで分割し，それぞれをデータベースに登録
for line in open("user.tsv", "r"):
    (userId, userCompany, userDiscountRate) = tuple(line[:-1].split("\t"))
    if userDiscountRate.isdigit(): # 一行目のコメント対応．
        User.create(userId = userId,
                    userCompany = userCompany,
                    userDiscountRate = int(userDiscountRate))
