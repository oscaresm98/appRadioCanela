import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'environments/environment';
import { take } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class RadioDataService {

  private URL_RADIO=environment.REMOTE_BASE_URL+ environment.RADIO_URL;
  private redondaData:any={};
  
  public getRadioRedondaData(){
    return this.redondaData;
  }

  constructor(private http: HttpClient) { }
  obtenerRadioRedondaRequest(){
    return new Promise((resolve)=>{
      this.http.get(this.URL_RADIO).pipe( take(1) ).subscribe({
        next:(res:any)=>{
          if (res != null) {
            const radio=res.find((radio)=>radio.nombre=="La radio Redonda")
            this.redondaData=radio;
            const data = { resCode: 0};
            resolve(data);
          }
        },
        error: (err) => {
          console.log(err);
          const data = { resCode: -1, error: err };
          resolve(data);
        },
      })
    });
  }
}
