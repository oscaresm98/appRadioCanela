/* eslint-disable @typescript-eslint/member-ordering */
import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthenticationAPIService, AuthenticationFirebaseService } from 'app/services/authentication.service';
import { DataService } from 'app/services/data/data.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.page.html',
  styleUrls: ['./login.page.scss'],
})
export class LoginPage implements OnInit {
  showPassword = false;
  loginForm = new FormGroup({
    email: new FormControl('', [Validators.required, Validators.email]),
    password: new FormControl('', [Validators.required, Validators.minLength(8)])
  });

  constructor(private router: Router, private authFireService: AuthenticationFirebaseService,
    private authApiService: AuthenticationAPIService, private data: DataService) { }

  ngOnInit() {
  }

  onLogin(form: any) {
    if (this.loginForm.valid ) {
      this.data.postLogin(form).subscribe(res => {
        console.log(res);
      });

      this.router.navigate(['/tabs']);
    }
  }

  public showHide(): void {
    this.showPassword = !this.showPassword;
  }

  get errorControl() {
    return this.loginForm.controls;
  }

  async signInWithGoogle() {
    try {
      const response = await this.authFireService.loginGoogle();
      console.log(response);
    } catch (error) {
      console.error(this.manageError(error));
    }
  }

  async signInWithFacebook() {
    try {
      const response = await this.authFireService.loginFacebook();
      console.log(response);
    } catch (error) {
      console.error(this.manageError(error));
    }
  }

  async signInWithApple() {
    try {
      const response = await this.authFireService.authApple();
      console.log(response);
    } catch (error) {
      console.error(this.manageError(error));
    }
  }

  private manageError(error: any){
    const message = error.error.non_field_errors[0];
    const code = error.status;
    switch (message) {
      case 'User is already registered with this e-mail address.':
        return `ERROR: ${code} \n Este correo ya ha sido registrado por un usuario.`;
      default:
        break;
    }
    return error;
  }

}
