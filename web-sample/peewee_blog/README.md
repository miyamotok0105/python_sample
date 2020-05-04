
# WIP


```
touch 

sqlite3 sqlite.db
```


```

```



### route list


```
$ python
>>> from app import app
>>> 
>>> app.url_map
Map([<Rule '/logout/' (GET, POST, HEAD, OPTIONS) -> logout>,
 <Rule '/create/' (GET, POST, HEAD, OPTIONS) -> create>,
 <Rule '/drafts/' (GET, HEAD, OPTIONS) -> drafts>,
 <Rule '/login/' (GET, POST, HEAD, OPTIONS) -> login>,
 <Rule '/' (GET, HEAD, OPTIONS) -> index>,
 <Rule '/static/<filename>' (GET, HEAD, OPTIONS) -> static>,
 <Rule '/<slug>/edit/' (GET, POST, HEAD, OPTIONS) -> edit>,
 <Rule '/<slug>/' (GET, HEAD, OPTIONS) -> detail>])
```

