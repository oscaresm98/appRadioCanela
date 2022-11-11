import { Component, OnInit } from '@angular/core';
import { HttpErrorResponse } from '@angular/common/http';
import { AuthService } from 'app/services/auth.service';
import { DataService } from 'app/services/data/data.service';
import { UsuarioService } from 'app/services/usuario.service';
import { DialogsController } from 'app/services/utils/dialogsController';
import { ProfilerForm } from 'app/shared/profile-form';

@Component({
  selector: 'app-my-account',
  templateUrl: './my-account.component.html',
  styleUrls: ['./my-account.component.scss'],
})
export class MyAccountComponent implements OnInit {

  profile: ProfilerForm = {
    first_name: 'Nombre',
    last_name: 'Apellido',
    username: 'Username',
    email: 'example@mail.com',
    phone: '099999999',
    cedula: 'xxxxxxxxxx',
    date_birth: 'dd/mm/yyyy',
    gender: 'Masculino',
  };

  //DATOS LOCALES
  first_name: string;
  last_name: string;
  username: string;
  email: 'example@mail.com';
  phone: string;
  cedula: string;
  date_birth: string;
  gender: string;

  constructor(
    private userService: UsuarioService,
    private authService: AuthService,
    private dialogsCtrl: DialogsController
  ) { }

  ngOnInit() {
    const load = this.dialogsCtrl.createLoadingDialog('Cargando...').then(dialog => {
      dialog.present();
      return dialog;
    });

    this.userService.getUserData().subscribe(
      resp => {
        this.profile = this.mapDataOfUser(resp);
      },
      (error: HttpErrorResponse) => {
        let message: string;
        if (error.status === 403) {
          message = 'No has iniciado sesion por lo que no se pueden mostrar un perfil';
        }
        else {
          message = error.message;
        }
        this.dialogsCtrl.createAlertError(message).then(alert => alert.present());
      }
    );
    load.then(dialog => dialog.dismiss());
  }

  private mapDataOfUser(response: any) {
    return {
      first_name: response.first_name,
      last_name: response.last_name,
      username: response.username,
      email: response.email,
      phone: (!response.telefono) ? '099999999' : response.telefono,
      cedula: (!response.cedula) ? 'xxxxxxxxxx' : response.cedula,
      date_birth: (!response.fechaNacimiento) ? 'dd/mm/yyyy' : response.fechaNacimiento,
      gender: (!response.sexo) ? 'None' : response.sexo,
    } as ProfilerForm;
  }

}
