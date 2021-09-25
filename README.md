# Django-Embed-Video-Testing

   
<a id='home'></a>
__Choose a language that suits you__

<a href='#uzb'>O'zbekcha</a>   or <a href='#us'>English</a>


#### English 
<a id="us"></a>
This is what I have done through Django’s Embed Video library which can be of great help to anyone using it as a simple guide for this textbook.

The use of this technology provides great convenience for the programmer.

Install the requirments.txt file to view the program

>Download Django Embed Video Library
`pip install django-embed-video`
`pip install git+https://github.com/jazzband/django-embed-video`

View the code of the program in the HTML file

```html+django
{% load embed_video_tags %}

<!-- The video tag: -->
{% video item.video as my_video %}
  URL: {{ my_video.url }}
  Thumbnail: {{ my_video.thumbnail }}
  Backend: {{ my_video.backend }}

  {% video my_video "large" %}
{% endvideo %}

<!-- Or embed shortcut: -->
{% video my_video '800x600' %}

```


> Location in the model.py file in your program
```python
from django.db import models
from embed_video.fields import EmbedVideoField

class Item(models.Model):
    video = EmbedVideoField()  # same like models.URLField()
```


<a href="https://github.com/jazzband/django-embed-video">Read more about Django Embed Video Library Github </a>

<a href="https://django-embed-video.readthedocs.io/en/latest/">Read more about Django Embed Video Library  documentation </a>

### Photo 
![Capture](https://user-images.githubusercontent.com/76002783/134783304-b7cfaddf-cebd-4948-8f0d-5d436c9a8d29.PNG)

![id video edit](https://user-images.githubusercontent.com/76002783/134783316-ade06442-ddf3-4f36-80db-ba1cfd0ecf93.PNG)

![admin sections](https://user-images.githubusercontent.com/76002783/134783301-98adeaf1-0032-4ab0-8827-4e85f12d47f5.PNG)


___
### <a href='#home'>⬆️⬆️ Back to top ⬆️⬆️</a>
___

#### O'zbekcha 
<a id="uzb"></a>
Bu men Djangoning Embed Video kutubxonasi orqali qilgan ishim, bu darslik uchun oddiy qo'llanma sifatida ishlatgan har bir kishiga katta yordam berishi mumkin.

Ushbu texnologiyadan foydalanish dasturchi uchun katta qulaylik yaratadi.

Dasturni ko'rish uchun requirements.txt faylini o'rnating

>Django Embed video kutubxonasini yuklab oling
`pip install django-embed-video `
`pip install git+https://github.com/jazzband/django-embed-video`


HTML faylida dastur kodini ko'ring

```html+django
{% load embed_video_tags %}

<!-- The video tag: -->
{% video item.video as my_video %}
  URL: {{ my_video.url }}
  Thumbnail: {{ my_video.thumbnail }}
  Backend: {{ my_video.backend }}

  {% video my_video "large" %}
{% endvideo %}

<!-- Or embed shortcut: -->
{% video my_video '800x600' %}

```

> Dasturingizdagi model.py fayildagi joylashuvi

```python
from django.db import models
from embed_video.fields import EmbedVideoField

class Item(models.Model):
    video = EmbedVideoField()  # modellar bilan bir models.URLField()
```

<a href="https://github.com/jazzband/django-embed-video">Django Embed Video kutibhonasi haqida ko'proq o'qing</a>

<a href="https://django-embed-video.readthedocs.io/en/latest/">Django Embed Video Library hujjatlari haqida ko'proq o'qing</a>

### Fotosuratlari 
![Capture](https://user-images.githubusercontent.com/76002783/134783304-b7cfaddf-cebd-4948-8f0d-5d436c9a8d29.PNG)

![id video edit](https://user-images.githubusercontent.com/76002783/134783316-ade06442-ddf3-4f36-80db-ba1cfd0ecf93.PNG)

![admin sections](https://user-images.githubusercontent.com/76002783/134783301-98adeaf1-0032-4ab0-8827-4e85f12d47f5.PNG)

___

### <a href='#home'>⬆️⬆️ Tepaga qaytish ⬆️⬆️</a>
