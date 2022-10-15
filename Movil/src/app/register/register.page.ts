import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators, } from '@angular/forms';
import { Router } from '@angular/router';
import { AlertController } from '@ionic/angular';
import { AuthService } from 'app/services/auth.service';
import { DataService } from 'app/services/data/data.service';
import { IUsuario } from 'app/shared/usuario.interface';
import { from } from 'rxjs';

@Component({
  selector: 'app-register',
  templateUrl: './register.page.html',
  styleUrls: ['./register.page.scss'],
})
export class RegisterPage implements OnInit {
  showPassword = false;
  samePassword: boolean = true;
  confPolicy: boolean = true;

  registerForm = new FormGroup({
    username: new FormControl('', Validators.required),
    first_name: new FormControl('', Validators.required),
    last_name: new FormControl('', Validators.required),
    email: new FormControl('', [Validators.required, Validators.email]),
    password: new FormControl('', [
      Validators.required,
      Validators.minLength(8),
    ]),
    conf_password: new FormControl('', [
      Validators.required,
      Validators.minLength(8),
    ]),
    policy: new FormControl('false', Validators.requiredTrue),
  });

  isSubmitted: boolean = false;

  constructor(
    private data: DataService,
    public formBuilder: FormBuilder,
    private alertController: AlertController,
    private router:Router,
    private authService: AuthService
  ) {}
  ngOnInit() {}

  public showHide(): void {
    this.showPassword = !this.showPassword;
  }

  get errorControl() {
    return this.registerForm.controls;
  }

  async presentAlertContraseñas() {
    const alert = await this.alertController.create({
      header: 'Oops!',
      message: 'Las contraseñas ingresadas no coinciden',
      buttons: ['OK'],
    });
    await alert.present();
  }

  async presentAlert() {
    const alert = await this.alertController.create({
      header: 'Oops!',
      message: 'Las contraseñas ingresadas no coinciden',
      buttons: ['OK'],
    });
    await alert.present();
  }

  public onRegister(form: any) {
    this.isSubmitted = true;

    if (form.password != form.conf_password) {
      this.presentAlertContraseñas();
    }

    if (form.policy == false) {
      this.confPolicy = false;
    } else {
      this.confPolicy = true;
    }

    if (form.password === form.conf_password && form.password != '' && form.conf_password != '') {
      this.data.postRegister(form).subscribe(res => {
        console.log(res)
      })
      console.log(form.password, form.conf_password);
      const user:IUsuario={
        username: form.username,
        first_name: form.first_name,
        last_name: form.last_name,
        email: form.email,
        password: form.password
      }
      this.authService.createUser(user).then(
        async (data:any)=>{
          if (data.resCode == 0) {
            console.log("Ingreso perfecto");
            this.router.navigate(['/login']);
          } else {
            const alert = await this.alertController.create({
              header: 'Oops!',
              message: 'Este nombre de usuario ya existe',
              buttons: ['OK'],
            });
            await alert.present();
            console.log("ERROR!!!!!")
          }
        }
        );
      
    }
  }
  
}

