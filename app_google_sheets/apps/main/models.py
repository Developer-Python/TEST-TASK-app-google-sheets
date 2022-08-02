
# Модуль для работы с моделями
from django.db import models



class Table(models.Model):

	'''==========================='''
	'''       Модель: Таблица     '''
	'''==========================='''

	id = models.AutoField(primary_key=True)
	table_id = models.IntegerField('Номер строки № ', default=0)
	order_id = models.IntegerField('Заказ №', default=0)
	order_eu = models.IntegerField('Стоимость, $', default=0)
	order_ru = models.IntegerField('Стоимость, ₽', default=0)
	date = models.CharField(verbose_name='Срок поставки', default=0, max_length=10)

	def __str__(self):
		return f' {self.table_id}№ - Строка в таблице ( {self.date} ) '

	class Meta:
		verbose_name = 'новую строку'
		verbose_name_plural = '1) Таблица'
