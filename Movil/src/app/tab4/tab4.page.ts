import { Component, OnInit } from '@angular/core';
import { DataService } from 'app/services/data/data.service';
import { ProfilerForm } from 'app/shared/profile-form';

@Component({
  selector: 'app-tab4',
  templateUrl: './tab4.page.html',
  styleUrls: ['./tab4.page.scss'],
})
export class Tab4Page implements OnInit {

  constructor(private dataService: DataService) { }
  //EJEMPLO RESPUESTA
  profile: ProfilerForm = {
    first_name: 'Carlos',
    last_name: 'Apellido',
    username: 'Username',
    email: 'example@mail.com',
    phone: '099999999',
    cedula: 'xxxxxxxxxx',
    date_birth: 'dd/mm/yyyy',
    gender: 'Masculino',
    
  }

  //DATOS LOCALES
  first_name: string;
  last_name: string;
  username: string;
  email: 'example@mail.com';
  phone: string;
  cedula: string;
  date_birth: string;
  gender: string;
  ngOnInit() {
    /*
    THIS WILL WORK WHEN THE API DONE
    this.dataService.getDataUser().subscribe(res => {
      this.profile = res as ProfilerForm
      this.username = this.profile.username;
      this.first_name = this.profile.first_name;
      this.last_name = this.profile.last_name;
      this.phone = this.profile.phone;
      this.cedula = this.profile.cedula;
      this.gender = this.profile.gender;
      this.date_birth = this.profile.date_birth;
      this.email = this.profile.email;
    })*/
  }


}
