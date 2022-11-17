function asignarPermisosSeccion(nombreSeccion) {
    $(`.${nombreSeccion}-checkbox`).prop('checked', true)
}

function quitarPermisosSeccion(nombreSeccion) {
    $(`.${nombreSeccion}-checkbox`).prop('checked', false)
}