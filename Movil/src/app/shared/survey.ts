export interface Survey{
    id: number,
    titulo: string,
    descripcion: string,
    imagen: string,
    fecha_hora_inicio :string,
    fecha_hora_fin: string,
    estado: boolean,
    contestado:boolean,
    id_emisora: number
};