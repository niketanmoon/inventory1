from django.shortcuts import render
from django.http import HttpResponse
from .models import Computer
# Create your views here.
def home(request):
	template='home.html'
	context = {}
	
	return render(request,template,context)

def postdata(request):
	if request.method == 'POST':
		Type=request.POST['Type']
		Make=request.POST['Make']
		Modelnumber=request.POST['Modelnumber']
		Barcode=request.POST['Barcode']
		SerialNo=request.POST['SerialNo']
		ServiceNo=request.POST['ServiceNo']
		Warranty=request.POST['Warranty']
		EndofLife=request.POST['EndofLife']
		WorkstationName=request.POST['WorkstationName']
		Domain=request.POST['Domain']
		Assetownedby=request.POST['Assetownedby']
		Purchasedate=request.POST['Purchasedate']
		Acquisitiondate=request.POST['Acquisitiondate']
		Returndate=request.POST['Returndate']
		Invoicenumber=request.POST['Invoicenumber']
		Status=request.POST['Status']
		Location=request.POST['Location']
		Desknumber=request.POST.get('Desknumber','200')
		CPU=request.POST['CPU']
		Ram=request.POST['Ram']
		ExternalStorage=request.POST['ExternalStorage']
		GPU=request.POST['GPU']
		OS=request.POST['OS']
		
		Computer.objects.create(
			Type=Type,
			Make=Make,
			Modelnumber=Modelnumber,
			Barcode=Barcode,
			SerialNo=SerialNo,
			ServiceNo=ServiceNo,
			Warranty=Warranty,
			EndofLife=EndofLife,
			WorkstationName=WorkstationName,
			Domain=Domain,
			Assetownedby=Assetownedby,
			Purchasedate=Purchasedate,
			Acquisitiondate=Acquisitiondate,
			Returndate=Returndate,
			Invoicenumber=Invoicenumber,
			Status=Status,
			Location=Location,
			Desknumber=Desknumber,
			CPU=CPU,
			Ram=Ram,
			ExternalStorage=ExternalStorage,
			GPU=GPU,
			OS=OS,
		)
	return HttpResponse('Done!')



def retrievedata(request):
	post1=Computer.objects.all()
	template='home.html'
	return render(request,template,{'Type':Type})


