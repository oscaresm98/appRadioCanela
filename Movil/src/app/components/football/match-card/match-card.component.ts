import { Component, Input, OnInit, Output, EventEmitter } from '@angular/core';
import { FootballGame } from 'app/shared/football';

@Component({
  selector: 'app-match-card',
  templateUrl: './match-card.component.html',
  styleUrls: ['./match-card.component.scss'],
})
export class MatchCardComponent implements OnInit {
  @Input() matchFootball: FootballGame;
  @Output() selectMatch: EventEmitter<FootballGame> = new EventEmitter();

  constructor() {}

  ngOnInit() {}

  selected() {
    this.selectMatch.emit(this.matchFootball);
  }

  getFormatedDate(date: string) {
    return (new Date(date)).toLocaleDateString();
  }

}
