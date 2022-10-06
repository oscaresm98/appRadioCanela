import { Component, OnInit } from '@angular/core';
import { ModalController } from '@ionic/angular';
import { ModalFootballGameComponent } from 'app/components/football/modal-football-game/modal-football-game.component';
import { FootballService } from 'app/services/football.service';
import { MatchFootball } from 'app/shared/football';

@Component({
  selector: 'app-futbol-game',
  templateUrl: './futbol-game.page.html',
  styleUrls: ['./futbol-game.page.scss'],
})
export class FutbolGamePage implements OnInit {

  matchesView: MatchFootball[] = [];

  constructor(private footballGameService: FootballService, private modalCtrl: ModalController) { }

  ngOnInit() {
    this.getGamesToPlay();
  }

  async openModal(event: MatchFootball) {
    const modal =  await this.modalCtrl.create({
      component: ModalFootballGameComponent,
      componentProps: { matchFootball: event },
      cssClass: 'modal-match'
    });

    await modal.present();
  }

  getGamesToPlay() {
    this.matchesView = this.footballGameService.getAllMatches().slice(0, 3);
    console.log('Partidos por jugar');
  }

  getGamesPlayed() {
    this.matchesView = this.footballGameService.getAllMatches().slice(3);
    console.log('Partidos ya disputados');
  }


}
