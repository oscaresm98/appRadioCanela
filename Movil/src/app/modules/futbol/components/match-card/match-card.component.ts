import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import Constantes from 'app/modules/util/constantes';
import { FootballGame } from 'app/shared/football';

@Component({
  selector: 'app-match-card',
  templateUrl: './match-card.component.html',
  styleUrls: ['./match-card.component.scss'],
})
export class MatchCardComponent implements OnInit {
  @Input() matchFootball: FootballGame;
  @Input() seccion:string;
  @Output() selectMatch: EventEmitter<FootballGame> = new EventEmitter();
  public globalConstantes = Constantes;
  constructor() {}

  ngOnInit() {}

  selected() {
    this.selectMatch.emit(this.matchFootball);
  }

  getFormatedDate(date: string) {
    return (new Date(date)).toLocaleDateString();
  }
}
