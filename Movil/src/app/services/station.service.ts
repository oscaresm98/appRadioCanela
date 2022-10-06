/* eslint-disable @typescript-eslint/dot-notation */
/* eslint-disable @typescript-eslint/member-ordering */
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Station } from 'app/shared/station';
import { map } from 'rxjs/operators';

@Injectable({ providedIn: 'root' })
export class StationService {
  private url = 'https://gruporadios.pythonanywhere.com/api/emisoras';

  constructor( private http: HttpClient ) {}

  /**
   * Funcion que devuelve los datos necesarios para cada emisora
   *
   * @returns un Observable de un array de objetos de tipo Station el cual contiene los datos necesarios para la transmision
   */
  getStationsInfo() {
    return this.http.get(this.url).pipe(
      map((res: any) => (res as any[]).map(this.getDataEachStation))
    );
  }

  /**
   * Obtiene la informacion necesaria de el objeto que se pasa en el parametro
   *
   * @param data Objeto de tipo <any> con datos de la API
   * @returns un objeto Station que se usara en el componente
   */
  private getDataEachStation(data: any): Station {
    return {
      id: data.id,
      name:data.nombre,
      image:data.logotipo,
      dial: `${data.frecuencia_dial} ${data.tipo}`,
      url: data.url_streaming
    } as Station;
  }

}
