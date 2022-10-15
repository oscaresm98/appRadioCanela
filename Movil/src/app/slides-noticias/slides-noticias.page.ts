import { Component, OnInit } from '@angular/core';
import { AuthService } from 'app/services/auth.service';
import { DataService } from 'app/services/data/data.service';
import { delay } from 'rxjs/operators';

@Component({
  selector: 'app-slides-noticias',
  templateUrl: './slides-noticias.page.html',
  styleUrls: ['./slides-noticias.page.scss'],
})
export class SlidesNoticiasPage implements OnInit {

  constructor(private dataService: DataService) { }
  noticias:any[]=[];
  loading:boolean=true;
  ngOnInit() {
    this.dataService.obtenerNoticias().then(
      async (data:any)=>{
        if (data.resCode == 0) {
          this.noticias=this.dataService.getNoticias();
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
      );;
  }

}
