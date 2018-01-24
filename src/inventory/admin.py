from django.contrib import admin

# Register your models here.
from .models import Computer

class ComputerAdmin(admin.ModelAdmin):
	class Meta:
		model = Computer
	list_display = ('Type','Make','Modelnumber','Barcode','SerialNo','ServiceNo','Warranty','EndofLife','WorkstationName','Domain','Assetownedby','Purchasedate','Acquisitiondate','Returndate','Invoicenumber','Status','Location','Desknumber','CPU','Ram','ExternalStorage','GPU','OS')


admin.site.register(Computer,ComputerAdmin)		 
