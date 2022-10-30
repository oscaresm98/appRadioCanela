import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ModalController, LoadingController } from '@ionic/angular';
import Constantes from 'app/modules/util/constantes';
import { FootballService } from 'app/services/football.service';
import { FootballGame } from 'app/shared/football';
import { isLaterDate } from 'app/shared/utils';
import { ModalFootbalComponent } from '../modal-footbal/modal-footbal.component';

@Component({
  selector: 'app-partidos',
  templateUrl: './partidos.component.html',
  styleUrls: ['./partidos.component.scss'],
})
export class PartidosComponent implements OnInit {

  matchesView: FootballGame[] = [];
  seccion:string=Constantes.ESTADO_PARTIDO_POR_JUGAR;
  public globalConstantes = Constantes;
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
      component: ModalFootbalComponent,
      componentProps: { matchFootball: event, seccion:this.seccion },
      cssClass: ['modal-match', isLaterDate(event.fecha_evento) ? 'large-modal-football': 'normal-modal-football'],
    });

    console.log('Modal destruido');
    modal.onDidDismiss().then(data => {
      try {
        this.router.navigate(['/principal/equipo', data.data.idTeam]);
      } catch (error) {
        // console.error(error);
      }
    });

    await modal.present();
  }

  async getGamesToPlay() {
    this.seccion=Constantes.ESTADO_PARTIDO_POR_JUGAR;
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
    this.seccion=Constantes.ESTADO_PARTIDO_DISPUTADO;
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
