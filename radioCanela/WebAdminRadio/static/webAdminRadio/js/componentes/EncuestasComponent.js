function encuestaSubida(datos) {
    const event = new CustomEvent('encuesta-subida', {
        detail: {
            datosFormulario: datos
        }
    });

    document.dispatchEvent(event);
}

const app = new Vue({
    el: '#app',
    delimiters: ["[[","]]"],
    data: {        
        tituloEncuesta: '',
        fechaInicio: '',
        fechaFin: '',
        imagenEncuesta: null,
        preguntas: [
            {
                id: null,
                titulo:'',
                tipo: '',
                opciones: [
                    { enunciado: null }
                ]
            },
        ],
        envio: false,
    },
    methods: {
        agregarPregunta() {
            this.preguntas.push(
                {
                    id: null,
                    titulo: '',
                    tipo: '',
                    opciones: [
                        { enunciado: null }
                    ]
                }
            );
        },
        
        eliminarPregunta(indice) {
            this.preguntas.splice(indice, 1);
        },

        agregarOpcionPregunta(indice) {
            this.preguntas[indice].opciones.push({ enunciado: null });
        },

        eliminarOpcionPregunta(indice) {
            this.preguntas[indice].opciones.pop();
        },

        imprimirJSON() {
            console.log(this.preguntas);
            var parsedobj = JSON.parse(JSON.stringify(this.preguntas))
            console.log(parsedobj)
        },

        actualizarImagen(evento){
            this.imagenEncuesta = evento.target.files[0];
        },

        enviarFormulario(e){
            e.preventDefault();
            
            let preguntasEncuesta = JSON.stringify(this.preguntas);
            
            $(e.target).append(`<textarea hidden name="preguntas">${preguntasEncuesta}</textarea>`); //Agregamos un textarea para contener el string del json de las preguntas
            $(e.target).submit();
            
            return true;
        }
    }
});