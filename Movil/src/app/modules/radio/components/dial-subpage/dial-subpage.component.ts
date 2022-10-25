import { Component, Input, OnInit } from '@angular/core';
import { LoadingController, AlertController } from '@ionic/angular';
import { RadioService } from 'app/services/radio/radio.service';

import { Station } from 'app/shared/station';

@Component({
  selector: 'app-dial-subpage',
  templateUrl: './dial-subpage.component.html',
  styleUrls: ['./dial-subpage.component.scss'],
})
export class DialSubpageComponent implements OnInit {
  @Input() station!: Station;
  @Input() playerIndex!: number;
  isPlaying = false;
  isLiking=false;

  constructor(
    public radioService: RadioService,
    private loadingCtrl: LoadingController,
    private alertCtrl: AlertController) { }

  ngOnInit() {}

  playPauseRadio() {
    if(!this.radioService.radioPlayer) {
      this.showLoading(); // Mostramos la senal de cargando
      this.radioService.setRadioPlayer(
        this.station.url_streaming,
        () => this.loadingCtrl.dismiss(),
        () => {
          this.showAlert(); // Mostramos una alerta
          this.isPlaying = false;
          this.radioService.radioPlayer = undefined;
        }
      );
    }

    if(!this.isPlaying) {
      this.radioService.playRadio(this.station.frecuencia_dial);
      this.isPlaying = true;
    }
    else {
      this.radioService.pauseRadio();
      this.isPlaying = false;
    }

  }

  /**
   * Mostrar ventana emegente de cargando cuando se inicia la radio
   */
  async showLoading() {
    const load = await this.loadingCtrl.create({
      message: 'Cargando...',
      spinner:'bubbles',
    });
    load.present();
  }

  /**
   * Mostrar alerta cuando hay un error al cargar la radio
   */
  async showAlert() {
    const alert = await this.alertCtrl.create({
      message: 'Error al cargar la transmision. Por favor intentelo mas tarde',
      buttons: ['OK'],
      mode: 'ios'
    });
    alert.present();
  }

  destroyRadio() {
    this.isPlaying = false;
    this.radioService.destroyRadio();
  }
  like(){
    this.isLiking=!this.isLiking;
  }

}
