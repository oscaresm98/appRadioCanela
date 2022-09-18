import { initializeApp } from "https://www.gstatic.com/firebasejs/9.9.4/firebase-app.js";
import {getStorage, ref, uploadBytes, getDownloadURL} from "https://www.gstatic.com/firebasejs/9.9.4/firebase-storage.js";
import * as name from "./componentes/notify.min.js"
let cargardatos = () =>{
    // credenciales para conectarse con firebase
    const firebaseConfig = {
        apiKey: "AIzaSyDr3NaNXjIt0IJQSPsQw-jZ2fJPVv-uGKs",
        authDomain: "radiocanela-13416.firebaseapp.com",
        databaseURL: "https://radiocanela-13416-default-rtdb.firebaseio.com",
        projectId: "radiocanela-13416",
        storageBucket: "radiocanela-13416.appspot.com",
        messagingSenderId: "182045702474",
        appId: "1:182045702474:web:b70eebc5f65ffcd320e9b3",
        measurementId: "G-GPTM872CX8"
      };
    $.notify.defaults({autoHideDelay: 1500, position:'r'})   
    // Inicializando Firebase
    const app = initializeApp(firebaseConfig);

    let btn = document.querySelector('#btnImagen');
    btn.addEventListener('click',async function() {
        let storage = getStorage(app); // Creando una referencia raíz
        let file = document.getElementById("imgSegmento").files[0];
        let a=true, i=1;
        let nombre = file.name
        while (a) { //seccion de codigo para renombrar archivo si ya se encuentra en firebase storage
            try {
                await getDownloadURL(ref(storage, "imagenes/"+nombre))
                nombre = file.name + `(${i})`;
                i++;
            } catch (error) {
                a = false;
            } 
        }
        let storageref = ref(storage, "imagenes/" + nombre); // Creando una referencia con el nombre de archivo
        uploadBytes(storageref, file).then((snapshot) => {// se sube el archivo
            $(function() {
                $(".error").notify("Carga exitosa!", "success"); // enviando un mensaje de confirmacion al usuario
            })
            getDownloadURL(storageref).then((url) => { // recurepando la direccion URL del archivo para asignarlo a una variable
                document.getElementById("imagen").value=url
            });
          });
    });
}

window.addEventListener('DOMContentLoaded', (event) => {
    cargardatos()
});