import { Injectable } from '@angular/core';
import { RadioService } from './radio/radio.player.service';

@Injectable({
  providedIn: 'root'
})
export class StopRadioService {

  constructor(private radioService:RadioService) { }

  public stopRadio() {
    this.radioService.destroyRadio();
  }
}
