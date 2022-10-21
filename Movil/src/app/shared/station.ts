/* eslint-disable @typescript-eslint/naming-convention */
export interface Station {
    id: number;
    radio: Radio;
    frecuencia_dial: string;
    url_streaming: string;
}


export interface Radio {
    nombre: string;
    imagen: string;
}
