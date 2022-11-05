import { Component, OnInit } from '@angular/core';
import { DataService } from 'app/services/data/data.service';
import { IPublicidad } from 'app/shared/publicidad.interface';

interface Image {
  src: string;
  alt: string;
}

@Component({
  selector: 'app-banner',
  templateUrl: './banner.component.html',
  styleUrls: ['./banner.component.scss'],
})
export class BannerComponent implements OnInit {
  images = [];
  publicidades:IPublicidad[];
  slideOpts = {
    speed: 400,
    loop:true,
    autoplay: {
      delay: 4000
    },
    allowTouchMove: false
  };

  constructor(private dataService:DataService) {
    
    
  }
  ngOnInit() {
    this.publicidades=this.dataService.getPublicidad();
    const publicidad1:IPublicidad={
      id: -1,
      titulo: 'default',
      cliente: 'none',
      descripcion: 'default',
      imagen: 'https://www.constantcontact.com/blog/wp-content/uploads/2021/04/img_60785f595c714-600x168.jpg',
      url: '',
      fecha_inicio: '',
      fecha_fin: ''
    }
    const publicidad2:IPublicidad={
      id: -1,
      titulo: 'default',
      cliente: 'none',
      descripcion: 'default',
      imagen: 'https://www.constantcontact.com/blog/wp-content/uploads/2021/04/img_60785f6151f0a-600x153.jpg',
      url: '',
      fecha_inicio: '',
      fecha_fin: ''
    }
    this.publicidades.push(publicidad1,publicidad2);
   }
  
}
