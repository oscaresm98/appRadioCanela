function cargarImagenEscudoLocal(equipoSeleccionado) {
    let urlImagen = equipoSeleccionado.getAttribute("data-img-escudo");
    let imgPreview = document.getElementById('preview-local');
    imgPreview.src = urlImagen;
}

function cargarImagenEscudoVisitante(equipoSeleccionado) {
    console.log(equipoSeleccionado);
    let urlImagen = equipoSeleccionado.getAttribute("data-img-escudo");

    console.log(urlImagen);
    let imgPreview = document.getElementById('preview-visitante');
    imgPreview.src = urlImagen;
}