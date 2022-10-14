import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'environments/environment';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private URL_TOKEN= environment.REMOTE_BASE_URL + environment.TOKEN_URL;

  private userData:any={};
  private token:string="";

  gteToken(){
    return this.token;
  }

  constructor(private http: HttpClient) { }

  public postLogin(username:string,password:string){
    const body:any={
      username:username,
      password:password
    }
    return new Promise((resolve)=>{
      this.http.post(this.URL_TOKEN,body).subscribe({
        next:(res:any)=>{
          if (res != null) {
            console.log("Obteniendo token usuario: ",res);
            this.token=res.token;
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
