import { Component, OnInit, ViewChild, ViewChildren } from '@angular/core';
import { IonInfiniteScroll, ModalController } from '@ionic/angular';
import { PhotoViewerComponent } from 'app/modules/Components/photo-viewer/photo-viewer.component';
import { DataService } from 'app/services/data/data.service';
import { ImageFile } from 'app/shared/media';
import { SwiperOptions } from 'swiper';

@Component({
  selector: 'app-galeria',
  templateUrl: './galeria.component.html',
  styleUrls: ['./galeria.component.scss'],
})
export class GaleriaComponent implements OnInit {
  @ViewChild(IonInfiniteScroll, {static: false}) infiniteScroll: IonInfiniteScroll;
  swiperConfig: SwiperOptions = {
    lazy: { checkInView:true },
    slidesPerView: 2,
    spaceBetween: 10,
    //loop: true,
  };
  allImagesList: any = [];
  imagesList: any = [];
  allILength;
  carouselImageList: any = [];
  constructor(
    private data: DataService,
    private modalCtrl: ModalController,
    ) { }
    ngOnInit() {
      this.data.getGallery().subscribe(e =>{
        this.allImagesList = e;
        this.allILength = this.allImagesList.length;
        for (let i = 0; i < this.allILength && i < 18; i++) {
          this.imagesList.push(this.allImagesList.pop());
        }
        for (let j = 0; j < 5; j++) {
          this.carouselImageList.push(this.imagesList.pop());
        }
      });
    }
    async openModal(event: ImageFile) {
      const modal =  await this.modalCtrl.create({
        component: PhotoViewerComponent,
        componentProps: { file: event},
        cssClass: ['modal-viewer'],
      });
      return await modal.present();
    }
    loadData(event) {
      setTimeout(() => {
        if (this.imagesList.length >= this.allILength) {
          event.target.complete();
          this.infiniteScroll.disabled = true;
          return;
        }
        for (let i = 0; i <= Math.floor(this.allImagesList.length/2); i++) {
          this.imagesList.push(this.allImagesList.pop() );
        }
        event.target.complete();
      }, 500);
    }

}
