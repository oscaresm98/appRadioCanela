import { Component, Input, OnInit } from '@angular/core';

interface Image {
  src: string;
  alt: string;
}

@Component({
  selector: 'app-carousel',
  templateUrl: './carousel.component.html',
  styleUrls: ['./carousel.component.scss'],
})
export class CarouselComponent implements OnInit {
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
      src: 'https://www.vidawellnessandbeauty.com/wp-content/uploads/2020/04/panel01-1.jpg',
      alt: 'placeholder1',
    };

    var img2: Image = {
      src: 'https://www.vidawellnessandbeauty.com/wp-content/uploads/2020/04/panel01-1.jpg',
      alt: 'placeholder2',
    };

    this.images.push(img1, img2);
    
  }
  ngOnInit() { }
}
