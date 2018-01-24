from django.db import models
# Create your models here.

from django.utils import timezone


type_choices = (
	('laptop','Laptop'),
	('workstation','Workstation'),
	('server','Server'),
	)

domain_choices= (
	('corp','Corp'),
	('prod','Prod'),
	)

asset_choices = (
	('legend','Legend'),
	('rental','Rental'),
	)

status_choices= (
	('active','Active'),
	('inactive','Inactive'),
	('decommissioned','Decommissioned'),
	('return','Return'),
	)

os_choices=(
	('window','Windows'),
	('linux','Linux'),
	)

class Computer(models.Model):
	Type = models.CharField(max_length= 50,choices=type_choices,default='Workstation')
	Make = models.CharField(max_length=30,default='DELL')
	Modelnumber = models.CharField(max_length=20,default='7810')
	Barcode = models.CharField(max_length=50,null=True)
	SerialNo = models.CharField(max_length=100,null=True,unique=True)
	ServiceNo = models.CharField(max_length=100,null=True)
	Warranty = models.CharField(max_length=20,default='1 Year') 
	EndofLife = models.CharField(max_length=50,null=True)
	WorkstationName=models.CharField(max_length=150,default='Name')
	Domain=models.CharField(max_length=10,choices=domain_choices,default='Prod')
	Assetownedby=models.CharField(max_length=8,choices=asset_choices,default='Legend')
	Purchasedate = models.DateField(null=True)
	Acquisitiondate = models.DateField(null=True)
	Returndate = models.DateField(null=True)
	Invoicenumber = models.CharField(max_length=100,null=True)
	Status = models.CharField(max_length=20,choices=status_choices,default='Active')
	Location= models.CharField(max_length=50,default='Pune')
	Desknumber=models.IntegerField(default=1)
	CPU=models.CharField(max_length=50,null=True)
	Ram = models.CharField(max_length=50,default='64 GB')
	ExternalStorage = models.CharField(max_length=50, default='1 TB')
	GPU = models.CharField(max_length=50,null=True)
	OS = models.CharField(max_length=20,choices=os_choices,default='Windows')

	def __str__(self):
		return self.Type