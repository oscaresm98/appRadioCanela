/* eslint-disable @typescript-eslint/naming-convention */
export interface FootballTeam {
    id: number;
    equipo: string;
    imagen: string;
    ciudad: string;
    descripcion: string;
    estado: boolean;
    redes_sociales: any[];
}

export interface StationFootball {
    id: number;
    frecuencia_dial: string;
    tipo_frecuencia: string;
    radio: string;
}

export interface FootballGame {
    id: number;
    emisoras: StationFootball[];
    id_torneo: any;
    id_equipo_local: any;
    id_equipo_visitante: any;
    hora_inicio: string;
    fecha_evento: string;
    lugar: string;
    descripcion: string;
    marcador: string;
    ptos_equipo_local: number;
    ptos_equipo_visitante: number;
    url_partido: string;
    plataforma: string;
    estadio: string;
    estado: boolean;
}
