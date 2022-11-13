import { Component, OnInit } from '@angular/core';
import { ModalController } from '@ionic/angular';
import { PodcastService } from 'app/services/podcast/podcast.service';
import { PlayerComponent } from '../player/player.component';

@Component({
  selector: 'app-podcast-bar',
  templateUrl: './podcast-bar.component.html',
  styleUrls: ['./podcast-bar.component.scss'],
})
export class PodcastBarComponent implements OnInit {

  constructor(public podcastService:PodcastService, private modalCtrl:ModalController) {}
  
  ngOnInit() {}

  async openModal() {
    const modal = await this.modalCtrl.create({
      component: PlayerComponent,
    });
    modal.present();
    const { data, role } = await modal.onWillDismiss();
  }

}