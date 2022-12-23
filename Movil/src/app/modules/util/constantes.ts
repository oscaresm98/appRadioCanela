import { Program, Programa, ProgramPerDia } from "app/shared/program";

export default class Constantes {
    public static ESTADO_PARTIDO_POR_JUGAR='porJugar';
    public static ESTADO_PARTIDO_DISPUTADO='disputado';
    public static DEFAULT_PROGRAMACION_PER_DAY:ProgramPerDia={
        dia: "Domingo",
        hora_inicio: "21:50:00",
        hora_fin: "22:50:00",
        programa: [
            {
                nombre: "Harta Pelota",
                descripcion: "Programa sobre las ultimas novedades del futbol",
                imagen: "https://firebasestorage.googleapis.com/v0/b/radiocanela-13416.appspot.com/o/imagenes%2Fhartapelota.jpg?alt=media&token=f4857495-e2d0-4654-a81a-e799bd1e6f66"
            }
        ],
        id: -1
    };
    public static DEFAULT_PROGRAMA:Program={
        id: -1,
        nombre: "",
        imagen: "",
        descripcion: "",
        horarios: []
    }

}