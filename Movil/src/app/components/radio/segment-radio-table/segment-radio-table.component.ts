/* eslint-disable @typescript-eslint/prefer-for-of */
/* eslint-disable @typescript-eslint/member-ordering */
/* eslint-disable @typescript-eslint/no-inferrable-types */
import {AfterViewChecked, Component, Input, OnChanges, OnDestroy, OnInit, SimpleChanges, ViewChild } from '@angular/core';
import { IonSegment } from '@ionic/angular';
import { DataService } from 'app/services/data/data.service';
import { Program } from 'app/shared/program';
import { SegmentItem } from 'app/shared/Segment';
import { Station } from 'app/shared/station';

import { moveSegment } from '../../../shared/utils';

@Component({
  selector: 'app-segment-radio-table',
  templateUrl: './segment-radio-table.component.html',
  styleUrls: ['./segment-radio-table.component.scss'],
})
export class SegmentRadioTableComponent implements OnInit, AfterViewChecked, OnDestroy, OnChanges {
  @Input() station: Station;
  @ViewChild('dayTabs') dayTabs: IonSegment;

  days: string[] = ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'];

  selectedDay: string = '';

  daySegments: Array<SegmentItem> = [];

  currentSegment: SegmentItem;

  intervalID: any;

  segments: Array<Program> = [];

  ready: boolean = false;

  constructor(private data: DataService) {
    this.selectedDay = this.getDayOfWeek();
  }

  ngOnInit() {
    this.data.getSegmentOfRadio().subscribe(res=>{
      this.segments = Object.values(res);
      this.changeProgramming(this.selectedDay);
    });
  }

  ngAfterViewChecked(): void {
    const elem = document.querySelector('ion-segment');
    this.focusInitialDay(elem);
  }

  ngOnChanges(changes: SimpleChanges): void {
    this.daySegments = null;
    this.changeProgramming(this.selectedDay);
  }

  ngOnDestroy(): void {
  }


  changeProgramming(day: any) {
    const items: Array<SegmentItem> = [];
    this.selectedDay = day;
    this.daySegments = [];

    let item: SegmentItem;
  /*   for (let index = 0; index < 5; index++) {
      item = {
        id:index,
        horaInicio: `${(new Date()).getHours()}:${(new Date()).getMinutes() + index}`,
        horaFin: `${(new Date()).getHours()}:${(new Date()).getMinutes() + index + 1}`,
        nombre:`Program ${index}`,
        imageUrl:'https://www.vidawellnessandbeauty.com/wp-content/uploads/2020/04/panel01-1.jpg'
      };
      items.push(item);
    } */

    for (let segment of this.segments) {
      for (let i = 0; i < segment.horarios.length; i++) {
        if (segment.horarios[i].dia == this.selectedDay){
          item = {
            id: segment.id,
            horaInicio: segment.horarios[i].hora_inicio,
            horaFin: segment.horarios[i].hora_fin,
            nombre: segment.nombre,
            imageUrl: segment.imagen
          };
          items.push(item);
        }
      }
    }
    this.daySegments = items;
    this.getCurrentSegment();
  }

  segmentChanged(e: any){
    setTimeout(() => moveSegment(e, `segment-${this.selectedDay}`), 200);
  }

  private getDayOfWeek(){
    return this.days[(new Date()).getDay()];
  }

  private getCurrentSegment(){
    const currentHour = `${(new Date()).getHours()}:${(new Date()).getMinutes()}`;
    for (const segment of this.daySegments) {
      if( currentHour <= segment.horaFin && currentHour >= segment.horaInicio){
        this.currentSegment = segment;
        break;
      }
    }
    this.ready = true;
  }

  private focusInitialDay(e: any){
    moveSegment(e, `segment-${this.selectedDay}`);
  }

}
