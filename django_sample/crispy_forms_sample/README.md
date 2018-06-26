


```
django-admin startproject crispy_forms_sample
python manage.py migrate
python manage.py runserver
```


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


```
python manage.py shell

from upload_image.models import Image
Image.objects.all()
Image.objects.all().delete()
Image.objects.filter(image_id=1).values()
Image.objects.filter(image_id=2).delete()

image_list = Image.objects.order_by('-published_date')[:5]
image_list
```