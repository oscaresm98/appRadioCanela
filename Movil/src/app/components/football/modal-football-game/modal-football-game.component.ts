import { Component, OnInit, Input, ViewEncapsulation } from '@angular/core';
import { Router } from '@angular/router';
import { ModalController } from '@ionic/angular';
import { FootballGame } from 'app/shared/football';
import { isLaterDate } from '../../../shared/utils';

@Component({
  selector: 'app-modal-team',
  templateUrl: './modal-football-game.component.html',
  styleUrls: ['./modal-football-game.component.scss'],
})
export class ModalFootballGameComponent implements OnInit {
  @Input() matchFootball: FootballGame;

  constructor(private modalCtrl: ModalController, private router: Router) { }

  ngOnInit() {}

  close() {
    this.modalCtrl.dismiss();
  }

  navigate(id: number) {
    this.modalCtrl.dismiss({idTeam: id});
  }

  getFormatedDate(date: string) {
    return (new Date(date)).toLocaleDateString();
  }

  showActionButtons = () => isLaterDate(this.matchFootball.fecha_evento);

}
