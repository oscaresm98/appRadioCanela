import { Component, OnInit } from '@angular/core';
import { LoadingController, ModalController } from '@ionic/angular';
import { ModalFootballGameComponent } from 'app/components/football/modal-football-game/modal-football-game.component';
import { FootballService } from 'app/services/football.service';
import { FootballGame } from 'app/shared/football';
import { Router } from '@angular/router';
import { isLaterDate } from 'app/shared/utils';

@Component({
  selector: 'app-futbol-game',
  templateUrl: './futbol-game.page.html',
  styleUrls: ['./futbol-game.page.scss'],
})
export class FutbolGamePage implements OnInit {

  matchesView: FootballGame[] = [];
  seccion:string='porJugar';
  constructor(
    private footballGameService: FootballService,
    private modalCtrl: ModalController,
    private router: Router,
    private loadingCtrl: LoadingController
  ) { }

  ngOnInit() {
    this.getGamesToPlay();
  }

  async openModal(event: FootballGame) {
    const modal =  await this.modalCtrl.create({
      component: ModalFootballGameComponent,
      componentProps: { matchFootball: event },
      cssClass: ['modal-match', isLaterDate(event.fecha_evento) ? 'large-modal-football': 'normal-modal-football'],
    });

    console.log('Modal destruido');
    modal.onDidDismiss().then(data => {
      try {
        this.router.navigate(['/futbol-team', data.data.idTeam]);
      } catch (error) {
        // console.error(error);
      }
    });

    await modal.present();
  }

  async getGamesToPlay() {
    this.seccion='porJugar';
    // this.matchesView = this.footballGameService.getAllMatches().slice(0, 3);
    const loading = await this.showLoadingGames();
    this.matchesView = [];

    this.footballGameService.getAllGamesToPlay().subscribe(
      resp => {
        this.matchesView = resp as FootballGame[];
        loading.dismiss();
      },
      error => loading.dismiss());
    console.log('Partidos por jugar');
  }

  async getGamesPlayed() {
    this.seccion='disputados';
    // this.matchesView = this.footballGameService.getAllMatches().slice(3);
    const loading = await this.showLoadingGames();
    this.matchesView = [];

    this.footballGameService.getAllGamesPlayed().subscribe(
      resp => {
        this.matchesView = resp as FootballGame[];
        loading.dismiss();
      },
      error => loading.dismiss());
    console.log('Partidos ya disputados');
  }

  private async showLoadingGames() {
    const loadingModal = await this.loadingCtrl.create({
      message: 'Cargando Partidos',
      mode: 'ios',
      spinner: 'circular'
    });
    await loadingModal.present();
    return loadingModal;
  }

}
