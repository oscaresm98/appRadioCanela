import { Component, Input, OnInit, Output, EventEmitter } from '@angular/core';
import { MatchFootball } from 'app/shared/football';

@Component({
  selector: 'app-match-card',
  templateUrl: './match-card.component.html',
  styleUrls: ['./match-card.component.scss'],
})
export class MatchCardComponent implements OnInit {
  @Input() matchFootball: MatchFootball;
  @Output() selectMatch: EventEmitter<MatchFootball> = new EventEmitter();

  constructor() {}

  ngOnInit() {}

  selected() {
    this.selectMatch.emit(this.matchFootball);
  }

}
