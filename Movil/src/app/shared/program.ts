export interface Program {
    id: number;
    nombre: string;
    imagen: string;
    idemisora?: Array<any>;
    descripcion: string;
    horarios: Array<any>;
}
export interface Programa {
    id?:number;
    nombre: string;
    descripcion:    string;
    imagen: string;
}

export interface ProgramPerDia{
    id: number;
    dia: string;
    hora_inicio: string;
    hora_fin:   string;
    programa:   Programa[];
}