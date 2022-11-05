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
  slideOpts = {
    speed: 400,
    loop:true,
    autoplay: {
      delay: 4000
    },
    allowTouchMove: false
  };
  ngOnInit() {
    this.noticias=this.dataService.getSlidesNoticias();
  console.log("Noticias slides: ",this.noticias)  
  }

}
