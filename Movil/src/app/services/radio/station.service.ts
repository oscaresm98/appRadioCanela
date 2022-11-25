/* eslint-disable @typescript-eslint/naming-convention */
/* eslint-disable @typescript-eslint/dot-notation */
/* eslint-disable @typescript-eslint/member-ordering */
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Station } from 'app/shared/station';
import { map } from 'rxjs/operators';

import { URL } from '../../../environments/environment';
import { RadioDataService } from './radio.data.service';
import { environment } from 'environments/environment';

@Injectable({ providedIn: 'root' })
export class StationService {

  constructor( private http: HttpClient,
    private radioService:RadioDataService ) {}


    getEmisoras() {
      const idRadio=this.radioService.getRadioRedondaData().id
      console.log("RADIO ID STATIONS: ",idRadio)
      const url=URL+'/api/radio/'+idRadio+'/emisoras'
      
    return new Promise((resolve) => {
      this.http.get<Station>(url, { withCredentials: true }).subscribe({
        next: (res: any) => {
          if (res != null) {
            console.log("EMISORAAS RADIO REDONDA: ",res)
            const data = { resCode: 0, resData:res };
            resolve(data);
          }
        },
        error: (err) => {
          console.log(err);
          let e;
          e = 'Error al intentar cargar los datos del usuario';
          const data = { resCode: -1, error: e };
          resolve(data)
        },
      })
    });
    }

}
