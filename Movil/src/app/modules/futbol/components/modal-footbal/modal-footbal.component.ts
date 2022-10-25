import { Component, Input, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ModalController } from '@ionic/angular';
import { FootballGame } from 'app/shared/football';
import { isLaterDate } from 'app/shared/utils';

@Component({
  selector: 'app-modal-footbal',
  templateUrl: './modal-footbal.component.html',
  styleUrls: ['./modal-footbal.component.scss'],
})
export class ModalFootbalComponent implements OnInit {
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
