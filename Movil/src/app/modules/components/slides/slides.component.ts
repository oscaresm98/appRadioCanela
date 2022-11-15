import { Component, OnInit } from '@angular/core';
import { AlertService } from 'app/services/alert.service';
import { DataService } from 'app/services/data/data.service';

@Component({
  selector: 'app-slides',
  templateUrl: './slides.component.html',
  styleUrls: ['./slides.component.scss'],
})
export class SlidesComponent implements OnInit {

  constructor(private dataService: DataService,
    private alertService: AlertService ) { }
  noticias:any[]=[];
  loading:boolean=true;
  slideOpts = {
    speed: 400,
    loop:true,
    autoplay: {
      delay: 4000
    },
    allowTouchMove: false
  };
  async ngOnInit() {
    await this.obtenerSlideNoticias();
    
  }
  private obtenerSlideNoticias(){
    this.dataService.obtenerSlidesNoticias().then(
      (data:any)=>{
        if (data.resCode == 0) {
          this.noticias=this.dataService.getSlidesNoticias();
          setTimeout(() => {
            this.loading=false;
          }, 1000);
        } else {
          this.alertService.displayErrorMessage("Error al cargar las noticias.");
        }
      }
      );;
  }

}
