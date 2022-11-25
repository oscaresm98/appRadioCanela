import { Component, Input, OnChanges, OnInit, SimpleChanges, ViewChild } from '@angular/core';
import { IonSlide, IonSlides } from '@ionic/angular';
import { SlidesService } from 'app/modules/services/slides.service';
import { AlertService } from 'app/services/alert.service';
import { DataService } from 'app/services/data/data.service';
import { BehaviorSubject, Observable, Subject } from 'rxjs';
import { SwiperOptions } from 'swiper';

@Component({
  selector: 'app-slides',
  templateUrl: './slides.component.html',
  styleUrls: ['./slides.component.scss'],
})
export class SlidesComponent implements OnInit,OnChanges {
  @ViewChild('slides',{ static: false }) slider:IonSlides;
  @Input() autoplay:boolean=true;
  noticias:any[]=[];
  loading:boolean=true;
  slideOpts = {
    speed: 400,
    loop:true,
    autoplay: {
      delay: 4000
    },
    //allowTouchMove: false
  };
  swiperConfig: SwiperOptions = { 
    lazy: { checkInView: true }, 
    pagination: false };
  constructor(private dataService: DataService,
    private alertService: AlertService,
    private slidesService:SlidesService ) {
      /*
      this.slidesService.EnteringObservable.subscribe(val => {
          console.log("ENTER OBSERVABLE: ",val)
        if(val==true && this.slider!=null) {
          this.slider.startAutoplay()
          this.slider.update()
          console.log('entrring')
        }
       
      });
      this.slidesService.LeavingObservable.subscribe(val => {
        console.log("LEAVING OBSERVABLE: ",val)
        if(val==true && this.slider!=null){
          this.slider.stopAutoplay()
          this.slider.update()
          console.log("leaving")
        }
      })*/
    }
  ngOnChanges(changes: SimpleChanges): void {
    if(this.autoplay==true && this.slider!=null){
      this.slider.update()
      this.slider.startAutoplay();
    }
    else if(this.autoplay==false && this.slider!=null){
      //this.slider.stopAutoplay()
    }
  }
    
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
            console.log(this.slider)
            //this.slider.stopAutoplay();
          }, 2000);
        } else {
          this.alertService.displayErrorMessage("Error al cargar las noticias.");
        }
      }
      );
      
  }
  setSlider(slides:IonSlides){
    this.slider=slides;
    //this.slider.stopAutoplay();
  }
  

}
