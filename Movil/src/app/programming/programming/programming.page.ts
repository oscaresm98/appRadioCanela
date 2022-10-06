import { Component, OnInit } from '@angular/core';
import { DataService } from 'app/services/data/data.service';
import { ActivatedRoute } from '@angular/router';
import { Host } from 'app/shared/host';
import { Program } from "../../shared/program";

@Component({
  selector: 'app-programming',
  templateUrl: './programming.page.html',
  styleUrls: ['./programming.page.scss'],
})
export class ProgrammingPage implements OnInit {
  Programas: Array<Program>;
  Programa: Program ;
  Locutores:Array<Host>;
  listo: boolean = false;
  
  constructor(private data:DataService,  private activatedRoute: ActivatedRoute) { 
    /* this.Programa = {
      id:30,
      nombre: 'Programa1',
      slogan: 'slogan1',
      descripcion: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer interdum arcu eu dolor commodo cursus.',
      image: 'https://www.vidawellnessandbeauty.com/wp-content/uploads/2020/04/panel01-1.jpg',
      horarios: [
        {
          dia:'Martes',
          fecha_inicio: "08:00:00",
          fecha_fin: "09:30:00"
        },
        {
          dia:'Jueves',
          fecha_inicio: "08:00:00",
          fecha_fin: "09:30:00"
        }
      ]
    } */

    //this.Locutores = [{name:"Carlos Salazar"}, {name:'Carla Suarez'}, {name:' Sara Bustamante'}];
  }

  ngOnInit() {
    let params = this.activatedRoute.snapshot.params;
    let id = parseInt(params["id"])
    this.loadData(id)
  }

  private loadData(id:number) {
    this.data.getPrograma().subscribe(res => {
      this.Programas = Object.values(res)
      for (let i = 0; i < this.Programas.length; i++) {
        if( id == this.Programas[i].id){
          this.Programa = this.Programas[i];
        }
        
      }
      this.data.getLocutoresPrograma(this.Programa.id).subscribe(res =>{
        this.Locutores = Object.values(res)
        this.listo  =true
      })
    })
  }

}
