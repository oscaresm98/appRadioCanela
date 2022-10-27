import { Component, OnInit } from '@angular/core';

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
  slideOpts = {
    speed: 400,
    loop:true,
    autoplay: {
      delay: 4000
    },
    allowTouchMove: false
  };

  constructor() {
    var img1: Image = {
      src: 'https://www.constantcontact.com/blog/wp-content/uploads/2021/04/img_60785f595c714-600x168.jpg',
      alt: 'placeholder1',
    };

    var img2: Image = {
      src: 'https://www.constantcontact.com/blog/wp-content/uploads/2021/04/img_60785f6151f0a-600x153.jpg',
      alt: 'placeholder2',
    };

    this.images.push(img1, img2);
    
  }
  ngOnInit() { }
}
