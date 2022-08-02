
# Модуль для работы с Админ панелью
from django.contrib import admin

# Модуль для работы с таблицей
from . models import Table

admin.site.register(Table)
