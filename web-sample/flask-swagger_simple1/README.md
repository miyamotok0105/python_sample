
# 概要


```
pip install -r requirements.txt
```

起動    

```
python app.py
```


# swaggerについて


これでイジイジしてgenerateしなさいよ。    
https://editor.swagger.io/
    


## swaggerの書き方

ファイルパスを変更した場合。    

```
paths:
  #URI
  /people:
    #getメソッド使用。
    get:
      #呼び出されるHTTP request関数を指定。
      #メソッド名を指定。
      operationId: read_all
      #ファイルの場所。modelsフォルダのpeopleファイルを使用する。
      x-swagger-router-controller: models.people
```

## 設定


```
http://localhost:8080/api/ui/#/
```


## GET /api/people

Try it out!をクリック。    


```
http://localhost:8080/api/people
```


## POST /api/people


```
{
  "fname": "miya",
  "lname": "kei"
}
```

Try it out!をクリック。    

## GET /api/people/{lname}

lname    

```
kei1
```

Try it out!をクリック。    


## PUT /api/people/{lname}

lname    

```
kei1
```

```
{
  "fname": "string",
  "lname": "string"
}
```

Try it out!をクリック。    


## DELETE /api/people/{lname}


lname    

```
kei1
```

Try it out!をクリック。    


## GET /api-models/user


```
http://localhost:8080/api-models/user
```


# 参考

https://qiita.com/Aruneko/items/2adbf12bb5bace32e002
