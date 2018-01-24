
var modal = document.getElementById('simpleModal');

//Get open modal Button
var addComputerBtn = document.getElementById('addComputerBtn');

//Get close button
var closeBtn=document.getElementsByClassName('closeBtn')[0];


//Listen for openclick
addComputerBtn.addEventListener('click', openModal); 


//Listen for close click
closeBtn.addEventListener('click', closeModal);

//Listen for outside click
window.addEventListener('click',outsideClick);
//function to open modal
function openModal(){
	modal.style.display = 'block';
}


//function to close modal
function closeModal(){
	modal.style.display = 'none';
}

function outsideClick(e){
	if(e.target == modal){
		modal.style.display = 'none';
	}
}

$(document).on('submit','#submitForm', function(e){
	e.preventDefault();
	
	$.ajax({
		type : "POST",
		url : 'postdata/',
		data : {
			Type:$('#typelist').val(),
			Make:$('#Make').val(),
			Modelnumber:$('#Modelnumber').val(),
			Barcode:$('#Barcode').val(),
			SerialNo:$('#SerialNo').val(),
			ServiceNo:$('#ServiceNo').val(),
			Warranty:$('#Warranty').val(),
			EndofLife:$('#EndofLife').val(),
			WorkstationName:$('#WorkstationName').val(),
			Domain:$('#Domain').val(),
			Assetownedby:$('#Assetownedby').val(),
			Purchasedate:$('#Purchasedate').val(),
			Acquisitiondate:$('#Acquisitiondate').val(),
			Returndate:$('#Returndate').val(),
			Invoicenumber:$('#Invoicenumber').val(),
			Status:$('#Status').val(),
			Location:$('#Location').val(),
			CPU:$('#CPU').val(),
			Ram:$('#Ram').val(),
			ExternalStorage:$('#ExternalStorage').val(),
			GPU:$('#GPU').val(),
			OS:$('#OS').val(),
			csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
		},
		success :function(){
			alert('Computer added successfully');
		},
				
	});
	
				
	});


$(document).ready(function(){
	e.preventDefault();
	$.ajax({
		type:'GET',
		url:'retrievedata/',
		success:function(){
			alert('Data retrieved'); 
		}
	})
});	
