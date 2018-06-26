


```
django-admin startproject crispy_forms_sample
python manage.py migrate
python manage.py runserver
```

http://localhost:8000/


```
python manage.py startapp upload_image
```

DBマイグレート

```
#DBマイグレート1
python manage.py makemigrations upload_image
python manage.py migrate upload_image
#DBマイグレート2
python manage.py makemigrations upload_image
python manage.py sqlmigrate upload_image 0001
python manage.py migrate
```


管理ユーザー作成


```
python manage.py createsuperuser

Username: admin
Email address: admin@admin.com
Password:
Password (again):
Superuser created successfully.
```

http://127.0.0.1:8000/admin/login/?next=/admin/


```
python manage.py shell

from upload_image.models import Image
Image.objects.all()
Image.objects.all().values()
Image.objects.all().delete()
Image.objects.filter(image_id=1).values()
Image.objects.filter(image_id=2).delete()
Image.objects.create(image_id=3)

image_list = Image.objects.order_by('-published_date')[:5]
image_list
```


# 画像ファイルアップロード

form.is_valid()で通らなくて「This field is required」エラーが出たり、色々ハマった。    
モデル部分はmodels.Modelを継承して作った。   
FileFieldの部分が画像ファイルへのパスを保存してるが、ここでハマった。    


```py:models.py
class Image(models.Model):
    # author = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
    image_id = models.AutoField(primary_key=True)
    # image_id = models.IntegerField()
    image_path = models.FileField(upload_to='./', null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return ""

```


ビューでも注意。    
ImageForm(request.POST, request.FILES)
のようにrequest.FILESを検証しておく必要あり。    


```py:view.py
def image_new(request):
    print("request", request)
    if request.method == "POST":
        print("post")
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            print("is valid")
            image = form.save(commit=False)
            image.save()
            return redirect(image_detail, pk=image.pk)
        else:
            print("not valid")
    else:
        print("get")
        form = ImageForm()
    return render(request, 'upload_image/image_edit.html', {'form': form})

```


htmlにも追記がいる。    
enctype="multipart/form-data"を入れとく。    


```html:image_edit.html
    <form method="POST" class="" enctype="multipart/form-data">{% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="save btn btn-default">Save</button>
    </form>
```

formのwidgetsにforms.FileInputを入れないと、「This field is required」が出てこれもハマった。    


```py:form.py
class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        # fields = ('image_path', 'created_date')
        fields = ('image_id', 'image_path', 'created_date', )
        # exclude = ('image_id', )
        widgets = {
            'created_date': forms.DateTimeInput(attrs={'class': 'datetime-input'}),
            # 'face_id':forms.HiddenInput(),
            'image_path': forms.FileInput(attrs={
                'class': "form-control",
            }),
        }
```



# 参考

https://qiita.com/narupo/items/6c9cd17914c6adfe1365




