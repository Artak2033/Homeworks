from django.db import models

class Category(models.Model):
	title = models.CharField('Category',max_length=50,blank=True,null=True)
	slug = models.SlugField('URL',unique=True)


	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'


class Man(models.Model):
	category = models.ForeignKey(Category,max_length=100,on_delete=models.CASCADE)
	first_name = models.CharField('Name',max_length=50)
	last_name = models.CharField(max_length=50)
	age = models.IntegerField(default=1)
	email = models.EmailField(unique=True)
	date = models.DateTimeField()
	photo = models.ImageField(upload_to='Man')
	about = models.TextField(blank=True,null=True)


	def __str__(self):
		return f'{self.id}  {self.first_name}'


	class Meta:
		verbose_name = 'Man'
		verbose_name_plural = 'Men'


class Woman(models.Model):
	category = models.ForeignKey(Category,max_length=100,on_delete=models.CASCADE)
	first_name = models.CharField('Name',max_length=50)
	last_name = models.CharField(max_length=50)
	age = models.IntegerField(default=1)
	email = models.EmailField(unique=True)
	date = models.DateTimeField()
	photo = models.ImageField(upload_to='Woman')


	def __str__(self):
		return f'{self.id}  {self.first_name}'


	class Meta:
		verbose_name = 'Woman'
		verbose_name_plural = 'Women'		