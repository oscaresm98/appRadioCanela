import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { LoginForm } from 'app/shared/login-form';
import { ProgramPerDia } from 'app/shared/program';
import { IPublicidad } from 'app/shared/publicidad.interface';
import { RegisterForm } from 'app/shared/register-form';
import { environment } from 'environments/environment';
import { Observable, take } from 'rxjs';
import { RadioDataService } from '../radio/radio.data.service';

@Injectable({
  providedIn: 'root'
})

export class DataService {

  url = ""
  private URL_NOTICIA = environment.REMOTE_BASE_URL + environment.NOTICIA_URL;

  private slidesNoticias: any[];
  private publicidad:IPublicidad[];

  constructor(private http: HttpClient,
    private radioDataService:RadioDataService) { }

  public getData() {
    return this.http.get(this.url)
  }
  public getSlidesNoticias(){
    return this.slidesNoticias;
  }
  public getPublicidad(){
    return this.publicidad;
  }


  public getProgramaRadioPerDay(idEmisora: number, dia: string) {
    return new Promise((resolve) => {
      this.http.get<ProgramPerDia[]>(
        environment.REMOTE_BASE_URL + '/api/emisora/' + idEmisora + '/dia/' + dia + '/programas')
        .pipe(take(1)).subscribe({
          next: (res: any) => {
            if (res != null) {
              const data = { resCode: 0,resData:res };
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
  public obtenerSlidesNoticias() {
    return new Promise((resolve) => {
      this.http.get(this.URL_NOTICIA).pipe(take(1)).subscribe({
        next: (res: any) => {
          if (res != null) {
            console.log("Obteniendo NOTicias: ", res);
            this.slidesNoticias = res;
            const data = { resCode: 0};
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
  public obtenerPublicidad() {
    const idRadio=this.radioDataService.getRadioRedondaData().id;

    return new Promise((resolve) => {
      this.http.get<IPublicidad[]>(
        environment.REMOTE_BASE_URL + '/api/radio/' + idRadio + '/publicidad')
        .pipe(take(1)).subscribe({
          next: (res: any) => {
            if (res != null) {
              this.publicidad=res;
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

  public getLocutoresPrograma(programa_id: number) {
    return this.http.get('https://gruporadios.pythonanywhere.com/api/' + 'segmentos/' + programa_id.toString() + '/locutores')
  }

  public getSegmentOfRadio() {
    return this.http.get('https://gruporadios.pythonanywhere.com/api/emisora/5/programas')
  }
  /*
    public postLogin(form:LoginForm):Observable<Response>{
      let url_login = this.url + "/login"
      return this.http.post<Response>(url_login, form)
    }
  */
  public postRegister(form: RegisterForm): Observable<Response> {
    let url_register = this.url + "/register"
    return this.http.post<Response>(url_register, form)
  }

  
  //NOTICIAS & TIPS
  public getNoticiaTip(id: number) {
    return this.http.get('https://gruporadios.pythonanywhere.com/api/noticia/' + id)
  }

  //NOTICIAS
  public getNoticias() {
    //return this.http.get('https://gruporadios.pythonanywhere.com/api/emisora/3/noticia')
    return this.http.get('https://gruporadios.pythonanywhere.com/api/noticia/noticia');
  }

  //TIPS
  public getTips() {
    return this.http.get('https://gruporadios.pythonanywhere.com/api/noticia/tip')
  }


  //GALLERY
  public getGallery() {
    return this.http.get('https://picsum.photos/v2/list?page=2&limit=100');
  }
}

