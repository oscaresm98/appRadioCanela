import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { IUsuario } from 'app/shared/usuario.interface';
import { environment } from 'environments/environment';
import { Storage } from '@ionic/storage-angular';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private URL_AUTH = environment.REMOTE_BASE_URL + environment.AUTH_URL;
  private URL_USERDATA = environment.REMOTE_BASE_URL + environment.USERDATA_URL;
  private URL_REGISTER = environment.REMOTE_BASE_URL + environment.REGISTER_URL;
  private URL_LOGOUT = environment.REMOTE_BASE_URL + environment.LOGOUT_URL;

  private userData: any = {};
  private token: string = "";
  private isAuth: boolean = false;
  private isGuest: boolean = false;

  getUserJson() {
    return this.userData;
  }
  getToken() {
    return this.token;
  }
  getIsAuth() {
    return this.isAuth;
  }
  getIsGuest() {
    return this.isGuest;
  }
  setGuest(isGuest: boolean) {
    this.isGuest = isGuest;
  }
  constructor(private http: HttpClient,
    private storage: Storage,) { }

  createUser(user: IUsuario) {
    const body: any = {
      ...user,
    }
    return new Promise((resolve) => {
      this.http.post(this.URL_REGISTER, body).subscribe({
        next: (res: any) => {
          if (res != null) {
            console.log("Post usuario usuario: ", res);
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

  postLogin(username: string, password: string) {
    const body: any = {
      username_email: username,
      password: password
    }
    return new Promise((resolve) => {
      this.http.post(this.URL_AUTH, body, { withCredentials: true }).subscribe({
        next: async (res: any) => {
          if (res != null) {
            this.token = res.jwt;
            this.storeUserToken(this.token);
            await this.storage.set('socialLogin', 'false');
            this.getUserData();
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
          this.isAuth = false;
        },
      })
    });

  }


  logoutRequest() {
    return new Promise((resolve) => {
      this.http.post(this.URL_LOGOUT, { withCredentials: true }).subscribe({
        next: (res: any) => {
          if (res != null) {
            const data = { resCode: 0 };
            resolve(data);
            this.isAuth = false;
          }
        },
        error: (err) => {
          console.log(err);
          let e;
          e = 'Error al intentar hacer el logout';
          const data = { resCode: -1, error: e };
          resolve(data);
        },
      })
    });
  }
  private getUserData() {
    return new Promise((resolve) => {
      this.http.get(this.URL_USERDATA, { withCredentials: true }).subscribe({
        next: (res: any) => {
          if (res != null) {
            console.log("Obteniendo  usuario: ", res);
            this.userData = res;
            const data = { resCode: 0 };
            this.isAuth = true;
            resolve(data);
          }
        },
        error: (err) => {
          console.log(err);
          let e;
          e = 'Error al intentar cargar los datos del usuario';
          const data = { resCode: -1, error: e };
          resolve(data);
          this.isAuth = false;
        },
      })
    });
  }
  private async storeUserToken(token: string) {
    await this.storage.set('jwt', token);
  }
}
