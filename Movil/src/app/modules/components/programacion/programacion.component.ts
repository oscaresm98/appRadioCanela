import { Component, Input, OnInit } from '@angular/core';
import Constantes from 'app/modules/util/constantes';
import { ProgramPerDia } from 'app/shared/program';

@Component({
  selector: 'app-programacion',
  templateUrl: './programacion.component.html',
  styleUrls: ['./programacion.component.scss'],
})
export class ProgramacionComponent implements OnInit {
  programacion:ProgramPerDia[]=[Constantes.DEFAULT_PROGRAMACION_PER_DAY];

  constructor() { }

  ngOnInit() {}
  isItPlaying(programa:ProgramPerDia){
    if(this.programacion.length<0) return false;
    if(programa==this.programacion[0]){
      return true
    }
    return false;
  }
  hourFormat(hora:string){
    let list=hora.split(":")
    return list[0]+':'+list[1];
  }
}
