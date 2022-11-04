import { Component, Input, OnChanges, OnInit, SimpleChanges } from '@angular/core';
import Constantes from 'app/modules/util/constantes';
import { DataService } from 'app/services/data/data.service';
import { RadioDataService } from 'app/services/radio/radio.data.service';
import { ProgramPerDia } from 'app/shared/program';
import { Station } from 'app/shared/station';

@Component({
  selector: 'app-programacion',
  templateUrl: './programacion.component.html',
  styleUrls: ['./programacion.component.scss'],
})
export class ProgramacionComponent implements OnInit, OnChanges {
  @Input() emisora:Station;

  programacion:ProgramPerDia[]=[Constantes.DEFAULT_PROGRAMACION_PER_DAY];

  constructor(private dataService:DataService) { }
  ngOnChanges(changes: SimpleChanges): void {
    console.log('ON CHNGES PROGRAMACION :',changes)
    this.ngOnInit();
  }

  ngOnInit() {
    if(this.emisora!=null){
      this.getProgramacion();
      console.log("EMISORA RECIBIDA: ",this.emisora)
    }
    
  }
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
  private getProgramacion(){
    const day:string=this.getTodayName();
    this.dataService.getProgramaRadioPerDay(this.emisora.id,day).then(
      async (data:any)=>{
        if (data.resCode == 0) {
          if(data.resData.length>1){
            console.log("Dentro del if ")
            this.programacion=data.resData;
            console.log("programacion dentro del if: ",this.programacion)
          }
          else{
            this.programacion=[Constantes.DEFAULT_PROGRAMACION_PER_DAY]
          }
        
        } else {
          console.log("Ocurrio un error al cargar la programacion")
        }
      }
      );
  }
  private getTodayName(){
      const date=new Date();
      const day=date.getDay();
      switch(day){
        case 1:
          return 'Lunes';
        case 2:
          return 'Martes';
        case 3:
          return 'Miércoles';
        case 4:
          return 'Jueves';
        case 5:
          return 'Viernes';
        case 6:
          return 'Sábado';
        case 7:
          return 'Domingo';
      }
  }
}

