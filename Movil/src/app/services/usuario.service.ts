import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { URL } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class UsuarioService {
  private userURL = URL + '/api/user/';

  constructor(
    private http: HttpClient,
  ) { }

  getUserData() {
    return this.http.get(this.userURL, { withCredentials: true });
  }
}
