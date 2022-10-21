/* eslint-disable object-shorthand */
/* eslint-disable @typescript-eslint/dot-notation */
import { Injectable } from '@angular/core';
import { ForegroundService } from '@awesome-cordova-plugins/foreground-service/ngx';
import { Howl, Howler } from 'howler';

@Injectable({
  providedIn: 'root'
})
export class RadioService {

  radioPlayer: Howl;

  constructor(private backgroundService: ForegroundService) {}

  setRadioPlayer(url: string, closeLoadingFunc: () => void, alertErrorFunc: () => void) {
    this.radioPlayer = new Howl({
      src:[url],
      html5: true,
      volume:1,
      preload: true,
      onload: () => console.log('Cargado'),
      onplay: () => closeLoadingFunc(),
      onplayerror: () => closeLoadingFunc(),
    });

    this.radioPlayer.on('loaderror', (id, msg) => {
      if(msg === 4) {
        console.log('Error');
        closeLoadingFunc();
        alertErrorFunc();
        this.backgroundService.stop();
      }
    });
  }


  playRadio(dial: string) {
    this.radioPlayer?.play();
    this.backgroundService.start('App Radio Forever', `Estas escuchando ${dial}`, 'drawable/fsicon');
  }

  pauseRadio(){
    this.radioPlayer?.pause();
    this.backgroundService.stop();
  }

  destroyRadio() {
    this.pauseRadio();
    this.radioPlayer = undefined;
    console.log('Destroy Radio');
  }

}
