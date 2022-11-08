import { ChangeDetectorRef, Component, Input, OnChanges, OnInit, SimpleChanges } from '@angular/core';
import Constantes from 'app/modules/util/constantes';
import { ProgramPerDia } from 'app/shared/program';

@Component({
  selector: 'app-programacion',
  templateUrl: './programacion.component.html',
  styleUrls: ['./programacion.component.scss'],
})
export class ProgramacionComponent implements OnInit,OnChanges {
  @Input() programacion:ProgramPerDia[]=[Constantes.DEFAULT_PROGRAMACION_PER_DAY];

  constructor(private changeDetector: ChangeDetectorRef) { }
  ngOnChanges(changes: SimpleChanges): void {
    this.ngOnInit();
  }

  ngOnInit() {
    this.changeDetector.detectChanges();
    console.log("Entrada prograamcion: ",this.programacion)
    if(this.programacion==null) this.programacion=[Constantes.DEFAULT_PROGRAMACION_PER_DAY];
    if(this.programacion.length<1) this.programacion=[Constantes.DEFAULT_PROGRAMACION_PER_DAY];
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
}
