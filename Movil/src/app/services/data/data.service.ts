import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { LoginForm } from 'app/shared/login-form';
import { RegisterForm } from 'app/shared/register-form';
import { environment } from 'environments/environment';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})

export class DataService {

  url = ""
  private URL_NOTICIA= environment.REMOTE_BASE_URL + environment.NOTICIA_URL;
  private noticias:any[];

  constructor(private http: HttpClient) { }

  public getData(){
    return this.http.get(this.url)
  }
  public getNoticias(){
    return this.noticias;
  }

  public getPrograma(){
    return this.http.get('https://gruporadios.pythonanywhere.com/api/segmentos/')
  }

  public getLocutoresPrograma(programa_id:number){
    return this.http.get('https://gruporadios.pythonanywhere.com/api/'+ 'segmentos/'+programa_id.toString()+'/locutores')
  }

  public getSegmentOfRadio(){
    return this.http.get('https://gruporadios.pythonanywhere.com/api/emisora/5/programas')
  }
/*
  public postLogin(form:LoginForm):Observable<Response>{
    let url_login = this.url + "/login"
    return this.http.post<Response>(url_login, form)
  }
*/
  public postRegister(form:RegisterForm):Observable<Response>{
    let url_register = this.url + "/register"
    return this.http.post<Response>(url_register, form)
  }
  
  public obtenerNoticias(){
    return new Promise((resolve)=>{
      this.http.get(this.URL_NOTICIA).subscribe({
        next:(res:any)=>{
          if (res != null) {
            console.log("Obteniendo NOTicias: ",res);
            this.noticias=res;
            const data = { resCode: 0 };
            resolve(data);
          }
        },
        error: (err) => {
          console.log(err);
          let e;
          e = 'Error al intentar cargar los datos del usuario';
          const data = { resCode: -1, error: e };
          resolve(data);
        },
      })
    });
  }
}

