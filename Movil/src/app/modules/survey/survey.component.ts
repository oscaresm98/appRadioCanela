import { Component, Input, OnInit } from '@angular/core';
import { Survey } from 'app/shared/survey';

@Component({
  selector: 'app-survey',
  templateUrl: './survey.component.html',
  styleUrls: ['./survey.component.scss'],
})
export class SurveyComponent implements OnInit {
  @Input() survey:Survey
  constructor() { }

  ngOnInit() {}

  getFormatedDate(date: string) {
    return (new Date(date)).toLocaleDateString();
  }
  getFormatedTime(date: string) {
    return date.slice(11,16);
  }
}
