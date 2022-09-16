import { initializeApp } from "https://www.gstatic.com/firebasejs/9.9.4/firebase-app.js";
import {getStorage, ref, uploadBytes, getDownloadURL} from "https://www.gstatic.com/firebasejs/9.9.4/firebase-storage.js";
import * as name from "./componentes/notify.min.js"
let cargardatos = () =>{
    // credenciales para conectarse con firebase
    const firebaseConfig = {
        apiKey: "AIzaSyCBnEfFvZLUBH-aI_OK6qACcdwEU5s1Po8",
        authDomain: "appradio-aa367.firebaseapp.com",
        databaseURL: "https://appradio-aa367-default-rtdb.firebaseio.com",
        projectId: "appradio-aa367",
        storageBucket: "appradio-aa367.appspot.com",
        messagingSenderId: "246344314591",
        appId: "1:246344314591:web:1d5f8ce1afb250c3c5036a",
        measurementId: "G-1RW3SNQ7LE"
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
                await getDownloadURL(ref(storage, nombre))
                nombre = file.name + `(${i})`;
                i++;
            } catch (error) {
                a = false;
            } 
        }
        let storageref = ref(storage, nombre); // Creando una referencia con el nombre de archivo
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