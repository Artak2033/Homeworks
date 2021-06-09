from django.db import models

class Person(models.Model):
	first_name = models.CharField('Name',max_length=20)
	last_name = models.CharField(max_length=20)
	age = models.IntegerField(default=1)


	def __str__(self):
		return f'{self.first_name} {self.last_name}'

	class Meta:
		verbose_name = 'Person'
		verbose_name_plural = 'People'


class Man(models.Model):
	first_name = models.CharField('Name',max_length=20)
	last_name = models.CharField(max_length=20)
	age = models.IntegerField(default=1)
	email = models.CharField(max_length=30,blank=True,null=True)
	adress = models.CharField(max_length=50)


	def __str__(self):
		return f'{self.id}->{self.first_name}'

	class Meta:
		verbose_name = 'Man'
		verbose_name_plural = 'Men'


class Woman(models.Model):
	first_name = models.CharField('Name',max_length=20)
	last_name = models.CharField(max_length=20)
	age = models.IntegerField(default=1)
	email = models.CharField(max_length=30,blank=True,null=True)
	adress = models.CharField(max_length=50)


	def __str__(self):
		return f'{self.id} - {self.first_name}'


	class Meta:
		verbose_name = 'Woman'
		verbose_name_plural = 'Women'

COLOR_CHOICE = (
	('Black','BLACK'),
	('White','WHITE'),
	('Red','RED'),
	('Green','GREEN'),
	('Blue','BLUE'),
	)

class Car(models.Model):
	car_name = models.CharField(max_length=20)
	car_color = models.CharField(max_length=20,choices=COLOR_CHOICE,default='Black')
	car_year = models.IntegerField(default=1)
	car_hp = models.IntegerField(default=1)
	car_about = models.TextField(blank=True,null=True)

	def __str__(self):
		return f'{self.car_name} - {self.car_year} - {self.car_color}'