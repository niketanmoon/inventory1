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




