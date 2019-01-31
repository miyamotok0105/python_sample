
# 概要


```
pip install -r requirements.txt
```

起動    

```
python app.py
```


# swaggerについて


http://localhost:8080/api/ui/#/


## GET /people

Try it out!をクリック。    

## POST /people


```
{
  "fname": "miya",
  "lname": "kei"
}
```

Try it out!をクリック。    

## GET /people/{lname}

lname    

```
kei1
```

Try it out!をクリック。    


## PUT /people/{lname}

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


## DELETE /people/{lname}


lname    

```
kei1
```

Try it out!をクリック。    




# 参考

https://qiita.com/Aruneko/items/2adbf12bb5bace32e002
