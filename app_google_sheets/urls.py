# Импортируем Админку
from django.contrib import admin
# Импортируем функцию path и include для работы с путями
from django.urls import path, include
# Импортируем настройки приложений
from django.conf import settings
# Импортируем функцию static для работы с путями статических файлов(изображения, архивы, торренты,иконки и т.д)
from django.conf.urls.static import static

urlpatterns = [
    path('', include('main.urls')),
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
