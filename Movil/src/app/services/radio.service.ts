import { Injectable } from '@angular/core';
import { ForegroundService } from '@awesome-cordova-plugins/foreground-service/ngx';
import { Station } from 'app/shared/station';
import { Howl } from 'howler';
import { StationService } from './station.service';

@Injectable({
  providedIn: 'root'
})
export class RadioService {

  radioPlayer: Howl;
  isPlaying = false;

  constructor(private backgroundService: ForegroundService) {
    this.backgroundService.start('App Radio Forever', 'Estas escuchando la transmision en vivo', 'drawable/fsicon');
  }

  setRadioPlayer(station: Station) {
    this.radioPlayer = new Howl({
      src:[station.url],
      html5: true,
      volume:1
    });
  }

  playRadio() {
    if(!this.isPlaying){
      this.radioPlayer?.play();
      this.isPlaying = true;
    }
  }

  pauseRadio(){
    if(this.isPlaying){
      this.radioPlayer.stop();
      this.isPlaying = false;
    }
  }

  destroyForeground() {
    this.backgroundService.stop();
  }

}
