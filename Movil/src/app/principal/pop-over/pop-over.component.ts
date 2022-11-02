import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AlertController, PopoverController } from '@ionic/angular';
import { AuthService } from 'app/services/auth.service';

@Component({
  selector: 'app-pop-over',
  templateUrl: './pop-over.component.html',
  styleUrls: ['./pop-over.component.scss'],
})
export class PopOverComponent implements OnInit {

  constructor(private router: Router,
    private popCtrl: PopoverController,
    private authService: AuthService,
    private alertController: AlertController) { }

  ngOnInit() { }
  logout() {
    if(this.authService.getIsGuest()){
      this.authService.setGuest(false);
      this.popCtrl.dismiss({
        'fromPopUp': "Cerar session"
      })
      this.router.navigate(['/login']);
    }
    else{
      this.authService.logoutRequest().then(
        async (data: any) => {
          if (data.resCode == 0) {
            this.router.navigate(['/login']);
            this.popCtrl.dismiss({
              'fromPopUp': "Cerar session"
            })
          } else {
            const alert = await this.alertController.create({
              header: 'Oops!',
              message: 'problema al cerrar sesion, revise su conexión.',
              buttons: ['OK'],
            });
            await alert.present();
          }
        }
      );
    }
    
  }
}
