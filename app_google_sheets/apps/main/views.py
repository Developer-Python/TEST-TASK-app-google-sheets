


# --------------------------- Подключение модулей ---------------------------- #

# Библеотека для работы с HTTP и т.д
import httplib2

# Библеотека для обработки URL
import requests

# Библеотеки для работы со временем и датами
import time
import datetime
from django.utils import timezone

# Библеотека для работы с запросами и редиректами
from django.http import Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

# Библеотека для работы с HTML
from bs4 import BeautifulSoup

# Библеотека для работы с подключением сервисов
from oauth2client.service_account import ServiceAccountCredentials

# Библеотека для работы с google-api-python-client
from googleapiclient.discovery import build

# Библеотека для работы с представлениями на основе классов предназначеный для отображения данных
from django.views.generic.base import View

# Модели приложенния
from . models import Table

# Настройки проекта
from django.conf import settings



# ------------------- Подключение API GOOGLE SHEETS -------------------------- #



# Файл с Token.json
CREDENTIALS_FILE = settings.CREDENTIALS_FILE

# ID документа (получаем его через URL)
spreadsheet_id = '1v_HLihRxv3-y2HAnFGIBIBRzRAq5aDTD1bLchdeJgLk'

# Авторизуемся и подключаем сервисы с которыми мы будем работать
credentials = ServiceAccountCredentials.from_json_keyfile_name(
	CREDENTIALS_FILE,
	['https://www.googleapis.com/auth/spreadsheets',
	 'https://www.googleapis.com/auth/drive'])

# Авторизуемся в системе
httpAuth = credentials.authorize(httplib2.Http())

# Указываем, что работать будем с "таблицами" и версией "v4"
service = build('sheets', 'v4', http = httpAuth)



# -------------------------- Основные функций -------------------------------- #


def create_table(i, values, usd):

    '''===================================='''
    '''     Функция: Создание таблицы      '''
    '''===================================='''

    # Создаём объекты
    table = Table.objects.create(
        table_id = values.get('values')[0][i],
        order_id = values.get('values')[1][i],
        order_eu = values.get('values')[2][i],
        order_ru = float(values.get('values')[2][i]) * usd,
        date = values.get('values')[3][i],
    )

    # Сохраняем в БД
    table.save()



def course_usd():

    '''======================================='''
    '''     Функция: Текущий курс доллара     '''
    '''======================================='''

    # В зависимости от курса доллара меняется и класс
    course_usd_up_down = (
	'value td-w-4 _bold _end mono-num _with-icon _down _green',
    'value td-w-4 _bold _end mono-num _with-icon _up _red',
    )

    # Делаем запрос на сайт - "https://cbr.ru/key-indicators/"
    resp = requests.get("https://cbr.ru/key-indicators/")

    # Парсим весь документ через парсер - 'lxml'
    soup = BeautifulSoup(resp.text, 'lxml')

    # Находим тег - "td" с классом - "value td-w-4...". В нём лежит значение текущего доллара
    for i in course_usd_up_down:

        # Проверяем какой из классов вернёт True
        if bool(soup.find("td", attrs={ "class" : f"{i}"})) == True:
            usd = str(soup.find("td", attrs={ "class" : f"{i}"}))

    # Возвращаем обработанную строку от всякого мусора с текущим долларам
    return round(float( usd[usd.find('>')+1:usd.rfind('<')].replace(',','.') ), 2)



def read_document(range):

    '''==================================='''
    '''     Функция: Чтения документа     '''
    '''==================================='''

    # Запроса на чтение документа из GOOGLE SHEETS
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=f'A1:E{range}',
        majorDimension='COLUMNS',
    ).execute()

    # Возвращаем словарь со встроеными массивами данных
    return values



# ------------------------ Работа с запросами Django ------------------------- #



def update(request):

    '''===================================='''
    '''     Функция: Обновление данных     '''
    '''===================================='''

    # Чтение документа(до [N] строк)
    values = read_document(100)

    # Текущий курс доллара
    usd = course_usd()

    # Удаляем все таблицы из БД
    Table.objects.all().delete()

    # Узнаём кол-во строк в документе и создаём диапозон(от, до)
    for i in range(1, len(values.get('values')[0])):
        create_table(i, values, usd)

    # Обновление страницы на главную после сохранения, чтобы сразу видеть результат
    return HttpResponseRedirect('/')



class TableView(View):

    '''======================================================'''
    '''     Класс: Корректирование и отображение таблицы     '''
    '''======================================================'''

    def get(self, request):

        # Точка отсчёта выполнения программы
        start_time = time.time()

        # Чтение документа(до [N] строк)
        values = read_document(100)

        # Текущий курс доллара
        usd = course_usd()

        # Узнаём кол-во строк в документе и создаём диапозон(от, до)
        for i in range(1, len(values.get('values')[0])):

            # Один раз создаёт строки, а последущие разы тока проверяет недостоющие
            try:
                # Проверяем есть строка или нету
                tables = Table.objects.get(table_id = i)

            except Exception:

                # Добовляем пропущенные строки
                create_table(i, values, usd)

        # Сортируем строки по порядку
        tables = Table.objects.order_by('table_id')

        # Точка подсчёта итоговой скорости выполнения программы
        finish_time = f"{time.time() - start_time}"[:6]

        # Отправляем данные - "tables, usd, finish_time", в "main.html"
        return render(request, "main/main.html", {"tables": tables, "usd": usd, "finish_time":finish_time })
