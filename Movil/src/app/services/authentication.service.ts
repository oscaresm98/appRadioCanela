/* eslint-disable quote-props */
/* eslint-disable @typescript-eslint/naming-convention */
import { Injectable } from '@angular/core';
import { AngularFireAuth } from '@angular/fire/compat/auth';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { FacebookAuthProvider, GoogleAuthProvider, AuthProvider, OAuthProvider } from 'firebase/auth';

/**
 * Clase para la autenticacion de cuentas mediante plataformas externas
 */
@Injectable({ providedIn: 'root'})
export class AuthenticationFirebaseService {

  constructor(private ngFireAuth: AngularFireAuth, private authApiService: AuthenticationAPIService) { }


  loginGoogle() {
    return this.authSocial(new GoogleAuthProvider(), 'google');
  }

  loginFacebook() {
    return this.authSocial(new FacebookAuthProvider(), 'facebook');
  }

  authApple() {
    return this.authSocial(new OAuthProvider('apple.com'), 'apple');
  }

  private async authSocial(socialProvider: AuthProvider, name: string) {
    const responseFirebase: any = await this.ngFireAuth.signInWithPopup(socialProvider);
    try {
      await this.authApiService.loginSocialAPI(responseFirebase.credential.accessToken, name);
      return responseFirebase.user;
    } catch (error) {
      throw error;
    }
  }

}

/**
 * Clase para la autenticacion de cuentas mediante la api de la radio
 */
@Injectable({providedIn: 'root'})
export class AuthenticationAPIService {
  private socialAuthUrl = 'http://127.0.0.1:8000/api/rest-auth/';
  private headers: HttpHeaders ;

  constructor(private http: HttpClient){
    this.headers = new HttpHeaders({'Content-Type': 'application/json; charset?utf-8', 'Accept':'*/*'});
  }

  async loginSocialAPI(responseToken: string, socialUrl: string) {
    const request = {access_token: responseToken};
    const loginUrl = this.socialAuthUrl + socialUrl + '/';
    // return await this.http.post(loginUrl, request, { headers: this.headers }).toPromise();

    try {
      return this.http.post(loginUrl, request, { headers: this.headers }).toPromise();
    } catch (error) {
      throw error;
    }
  }

}
