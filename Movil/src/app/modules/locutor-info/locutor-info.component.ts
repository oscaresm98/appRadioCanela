import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { DataService } from 'app/services/data/data.service';
import { Locutor } from 'app/shared/locutor.interface';

@Component({
  selector: 'app-locutor-info',
  templateUrl: './locutor-info.component.html',
  styleUrls: ['./locutor-info.component.scss'],
})
export class LocutorInfoComponent implements OnInit {

  constructor(private activatedRoute: ActivatedRoute,private dataService: DataService) { }
  idPrograma:number=-1;
  locutor:Locutor;
  async ngOnInit() {
    let params = this.activatedRoute.snapshot.params;
    let idPrograma = parseInt(params["idPrograma"]);
    const idLocutor = parseInt(params["idLocutor"]);
    
    await this.dataService.getLocutoresProgramaById(idPrograma).then(
      (data:any)=>{
        if (data.resCode == 0) {
          const locutores=data.resData;
          this.locutor=locutores.find(element => element.id==idLocutor);
        } else {
          console.log("ERROR AL OBTEBER Locutores")
        }
        
      }
      );
  }

}
