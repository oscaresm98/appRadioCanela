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
        _actualizar_tooltips(){
            setTimeout(() => $("[data-bs-toggle='tooltip']").tooltip(), 500);
        },

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
            this._actualizar_tooltips();
        },
        
        eliminarPregunta(indice) {
            this.preguntas.splice(indice, 1);
        },

        actualizarPreguntas(url) {
            fetch(url).then(res => res.json()).then(data => { this.preguntas = data })
                .catch(console.error);
        },

        agregarOpcionPregunta(indice) {
            this.preguntas[indice].opciones.push({ enunciado: null });
        },

        eliminarOpcionPregunta(indice) {
            this.preguntas[indice].opciones.pop();
        },

        imprimirJSON() {
            console.log(this.preguntas);
            var parsedobj = JSON.parse(JSON.stringify(this.preguntas));
            console.log(parsedobj);
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
