const RedSocial=  {
    data () {
      return {
        redes_sociales:[],
      }
    },
    methods:{
      agregarRegistro(){
        this.redes_sociales.push({'nombre': null,'link': null, 'username': null, esOtra:false})
      },
      eliminarRegistro(indice){
        this.redes_sociales.splice(indice,1)
      },
      verificarOtraRed(e,indice){
        this.redes_sociales[indice].nombre= e.target.value
        this.redes_sociales[indice].esOtra= (this.redes_sociales[indice].nombre == "Otra")
      }
    },
    mounted () {
      this.agregarRegistro()
    },
    template:/*html*/`
    <div>
      <div v-for="(red,index) in redes_sociales" v-bind:key="index" class="row">
        <div class="mb-2 col-3">
          <input v-model="red.username" v-bind:name="'red_social_username'" type="text" class="form-control" placeholder="Nombre de usuario">
        </div>
        <div class="mb-2 col-3">
            <input v-model="red.link" v-bind:name="'red_social_url'" type="url" class="form-control" placeholder="Url">
        </div>
        <div class="mb-2 col-3">
            <select @change="verificarOtraRed($event,index)" v-bind:name="'red_social_nombre'" class="form-select form-control" required>
                <option disabled selected value="">Red Social</option>
                <option value="Facebook">Facebook</option>
                <option value="Twitter">Twitter</option>
                <option value="Instagram">Instagram</option>
                <option value="Youtube">Youtube</option>
                <option value="Otra">Otra</option>
            </select>
        </div>
        <div v-if="red.esOtra == true" class="mb-2 col-3">
            <input v-model="red.nombre" class="form-control" v-bind:name="'red_social_nombre'" placeholder="Ingrese el nombre de la red social">
        </div>
        <div v-if="index != 0" class="mb-2 col-3">
            <button type="button" class="btn btn-primary" @click="eliminarRegistro(index)" >Eliminar</button>
        </div>
        <div class="mb-2 col-3">
            <button v-if="index == redes_sociales.length - 1" type="button" class="btn btn-primary" @click="agregarRegistro" >Agregar Nuevo</button>
        </div>
      </div>
    </div>
    `
  }

  /* Variable contenedora de la instancia del componente Red social*/
  var contenedorRedesSociales = new Vue({
    el: '#componente_redsocial',
    components: {
      'redsocial' : RedSocial
    }
  })