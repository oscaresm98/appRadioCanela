import { Component, OnInit } from '@angular/core';
import { DataService } from 'app/services/data/data.service';

@Component({
  selector: 'app-slides',
  templateUrl: './slides.component.html',
  styleUrls: ['./slides.component.scss'],
})
export class SlidesComponent implements OnInit {

  constructor(private dataService: DataService) { }
  noticias:any[]=[];
  loading:boolean=true;
  ngOnInit() {
    this.dataService.obtenerNoticias().then(
      async (data:any)=>{
        if (data.resCode == 0) {
          this.noticias=data.resData;
          console.log("NOTICIAS EXITOSAS: ",this.noticias)
          setTimeout(function () {
            console.log("YA PASO 5 SEGUNDOS")
            this.loading=false;
        }, 5000);
        
        } else {
          console.log("ERROR AL OBTEBER NOCTICIAS")
          this.loading=true;
        }
      }
      );
    }

}
