var name_error=document.getElementById('name-error');
var last_name_error=document.getElementById('last-name-error');
var id_error=document.getElementById('id-error')
var username_error=document.getElementById('username-error');
var birth_date_error=document.getElementById('birth-date-error');
var email_error=document.getElementById('email-error');
var cellphone_error=document.getElementById('cellphone-error');
var image_error=document.getElementById('image-error');
function validateName(){
    var name=document.getElementById('nombre').value;
    if(name.length==0){
        name_error.innerHTML='Este campo es requerido.'
        return false;
    }
    var expression=/^[A-Za-z]*[\s{1}]*[A-Za-z]*$/;
    if(!name.match(expression)){
        name_error.innerHTML='Nombre invalido.';
        return false;
    }
    name_error.innerHTML="<i class='fa-regular fa-circle-check'></i>"
    return true;
}
function validateLastName(){
    var last_name=document.getElementById('apellido').value;
    if(last_name.length==0){
        last_name_error.innerHTML='Este campo es requerido.'
        return false;
    }
    var expression=/^[A-Za-z]*[\s{1}]*[A-Za-z]*$/;
    if(!last_name.match(expression)){
        last_name_error.innerHTML='Apellido invalido.';
        return false;
    }
    last_name_error.innerHTML="<i class='fa-regular fa-circle-check'></i>"
    return true;
}
function validateID(){
    var id=document.getElementById('cedula').value;
    if(id.length==0){
        id_error.innerHTML='Este campo es requerido.'
        return false;
    }
    var expression=/^[0-9]{10}$/;
    if(!id.match(expression)){
        id_error.innerHTML='Cédula invalida.';
        return false;
    }
    id_error.innerHTML="<i class='fa-regular fa-circle-check'></i>"
    return true;
}
function validateUsername(){
    var username=document.getElementById('username').value;
    if(username.length==0){
        username_error.innerHTML='Este campo es requerido.'
        return false;
    }
    var expression=/^[A-Za-z]{1}[a-zA-Z0-9]*$/;
    if(!username.match(expression)){
        username_error.innerHTML='username invalido.';
        return false;
    }
    username_error.innerHTML="<i class='fa-regular fa-circle-check'></i>"
    return true;
}
// Fecha Nacimiento
var dateBirth= document.querySelector('#fechaNac');
var max=maxDateBirth();
dateBirth.setAttribute('max',max);

function maxDateBirth(){
    var dateObj = new Date();
    var month = dateObj.getUTCMonth() + 1; //months from 1-12
    var day = dateObj.getUTCDate();
    var year = dateObj.getUTCFullYear();
    year=year-18;
    return year + "-" + formatDate(month) + "-" + formatDate(day);
}
function formatDate(value){
    if(value<10 && value>0){
        return "0"+value;
    }
    return ""+value;
}
//Email
function validateEmail(){
    var email=document.getElementById('email').value;
    if(email.length==0){
        email_error.innerHTML='Este campo es requerido.'
        return false;
    }
    var expression=/^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$/;
    if(!email.match(expression)){
        email_error.innerHTML='correo invalido.';
        return false;
    }
    email_error.innerHTML="<i class='fa-regular fa-circle-check'></i>"
    return true;
}
//Telefono
function validateTelefono(){
    var telefono=document.getElementById('telefono').value;
    if(telefono.length==0){
        cellphone_error.innerHTML='Este campo es requerido.'
        return false;
    }
    var expression=/^[0-9]{10}$/;
    if(!telefono.match(expression)){
        cellphone_error.innerHTML='Teléfono invalido.';
        return false;
    }
    cellphone_error.innerHTML="<i class='fa-regular fa-circle-check'></i>"
    return true;
}
function submitData(){

    if(validateName() && validateLastName() && validateID() && validateEmail()&&
    validateUsername() && validateTelefono()) return true;
    return false;
}