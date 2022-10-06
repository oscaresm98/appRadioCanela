import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { LoginForm } from 'app/shared/login-form';
import { RegisterForm } from 'app/shared/register-form';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})

export class DataService {
  url = ""
  constructor(private http: HttpClient) { }

  public getData(){
    return this.http.get(this.url)
  }

  public getPrograma(){
    return this.http.get('https://gruporadios.pythonanywhere.com/api/segmentos/')
  }

  public getLocutoresPrograma(programa_id:number){
    return this.http.get('https://gruporadios.pythonanywhere.com/api/'+ 'segmentos/'+programa_id.toString()+'/locutores')
  }

  public getSegmentOfRadio(){
    return this.http.get('https://gruporadios.pythonanywhere.com/api/emisora/13/segmentos')
  }

  public postLogin(form:LoginForm):Observable<Response>{
    let url_login = this.url + "/login"
    return this.http.post<Response>(url_login, form)
  }

  public postRegister(form:RegisterForm):Observable<Response>{
    let url_register = this.url + "/register"
    return this.http.post<Response>(url_register, form)
  }
}

