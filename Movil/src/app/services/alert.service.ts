import { Injectable } from '@angular/core';
import { AlertController } from '@ionic/angular';

@Injectable({
  providedIn: 'root'
})
export class AlertService {

  constructor(private alertController: AlertController) { }
  async displayErrorMessage(error:string) {
    const alert = await this.alertController.create({
      header: 'Alert',
      subHeader: 'Error!!',
      message: error,
      buttons: ['OK'],
    });
    await alert.present();
  }
  
}
