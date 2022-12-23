import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { DataService } from 'app/services/data/data.service';
import { Locutor } from 'app/shared/locutor.interface';
import { Program, Programa } from 'app/shared/program';
import Constantes from '../util/constantes';

@Component({
  selector: 'app-programa-info',
  templateUrl: './programa-info.component.html',
  styleUrls: ['./programa-info.component.scss'],
})
export class ProgramaInfoComponent implements OnInit {
  
  programa:Program=Constantes.DEFAULT_PROGRAMA;
  locutores: Locutor[]=[];
  idPrograma:number=-1;
  constructor(private activatedRoute: ActivatedRoute,private dataService: DataService) { }

  async ngOnInit() {
    let params = this.activatedRoute.snapshot.params;
    let id = parseInt(params["id"])
    this.idPrograma=id;
    await this.dataService.getProgramaById(id).then(
      (data:any)=>{
        if (data.resCode == 0) {
          this.programa=data.resData;
        } else {
          console.log("ERROR AL OBTEBER NOCTICIAS")
        }
        
      }
      );
      await this.dataService.getLocutoresProgramaById(id).then(
        (data:any)=>{
          if (data.resCode == 0) {
            this.locutores=data.resData;
          } else {
            console.log("ERROR AL OBTEBER Locutores")
          }
          
        }
        );
  }

}
