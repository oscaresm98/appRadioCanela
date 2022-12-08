function obtenerUrlImagen(input, selectorElementoImagen) {
    if(input.files && input.files[0]){
        let lector = new FileReader();
        lector.onload = (e) => { $(selectorElementoImagen).attr('src', e.target.result); }
        lector.readAsDataURL(input.files[0]);
    }
}

function actualizarImagen(selectorInputArchivo, selectorElementoImagen) {
    $(selectorInputArchivo).change(function() {
        obtenerUrlImagen(this, selectorElementoImagen);
    }); 
}

