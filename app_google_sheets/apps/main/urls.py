
# Модуль для работы с путями
from django.urls import path

# Модуль для работы с функциями из "views"
from . import views

app_name = 'main'

urlpatterns = [
	path("", views.TableView.as_view(), name='table'),
	path('update/', views.update, name = 'update'),
]
