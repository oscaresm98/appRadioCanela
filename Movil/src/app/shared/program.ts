export interface Program {
    id: number;
    nombre: string;
    imagen: string;
    idemisora?: Array<any>;
    descripcion: string;
    horarios: Array<any>;
}
export interface ProgramDia{
    dia: string;
    hora_inicio: string;
    hora_fin:   string;
    nombre:     string;
    descripcion:    string;
    imagen:         string;
}