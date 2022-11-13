import { Component, OnInit, ViewChild } from '@angular/core';
import { IonRange, ModalController } from '@ionic/angular';
import { PodcastService } from 'app/services/podcast/podcast.service';

@Component({
  selector: 'app-player',
  templateUrl: './player.component.html',
  styleUrls: ['./player.component.scss'],
})
export class PlayerComponent implements OnInit {
  
  @ViewChild('range', { static : false}) 
  range: IonRange;

  constructor(private modalCtrl: ModalController, public podcastService:PodcastService) {}
  
  ngOnInit() {
  }

  cancel() {
    return this.modalCtrl.dismiss(null, 'cancel');
  }

  public seek() {
    let newValue = +this.range.value;
    let duration = this.podcastService.player.duration();
    this.podcastService.player.seek(duration * (newValue/100));
  }

  /* public updateProgress(){
    let seek = this.podcastService.player.seek();
    this.podcastService.progress = (seek / this.podcastService.player.duration()) * 100 || 0;
    setTimeout(() => {
      this.updateProgress();
    }, 1000)
  } */

}
