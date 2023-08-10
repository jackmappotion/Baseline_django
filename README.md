# Django_Baseline

## 1. start project

```
django-admin startproject config .
```

## 2. start app

```
django-admin startapp myapp
```

## 3. settings.py

```
# Application definition

INSTALLED_APPS = [
    'myapp.apps.MyappConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

## 4. urls.py

```
config/urls.py

---

from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
]

---------------------------------------------

myapp/urls.py

---
from django.urls import path
from .views import myapp_view
urlpatterns = [
    path("myapp_url",myapp_view),
]
```

## 5. views.py

```
from django.http import HttpResponse

def myapp_view(request):
    return HttpResponse("myapp_view")
```

## additionally
### Database - MySQL

```
config/settings.py

---

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost', 
        'USER': 'root',
        'PASSWORD': '1234',
        'PORT': '3306',
        'NAME': 'my_database', 
    }
}
```