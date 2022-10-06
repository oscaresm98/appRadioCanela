import { Component, OnInit, Input, ViewEncapsulation } from '@angular/core';
import { Router } from '@angular/router';
import { ModalController } from '@ionic/angular';
import { MatchFootball } from 'app/shared/football';

@Component({
  selector: 'app-modal-team',
  templateUrl: './modal-football-game.component.html',
  styleUrls: ['./modal-football-game.component.scss'],
})
export class ModalFootballGameComponent implements OnInit {
  @Input() matchFootball: MatchFootball;

  constructor(private modalCtrl: ModalController, private router: Router) { }

  ngOnInit() {}

  close() {
    this.modalCtrl.dismiss();
  }

  navigate(id: number) {
    this.close();
    this.router.navigate(['/futbol-team', id]);
  }

}
