import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';
import { CarouselComponent } from './carousel.component';

@NgModule({
  imports: [ CommonModule, FormsModule, IonicModule],
  declarations: [CarouselComponent],
  exports: [CarouselComponent]
})
export class CarouselComponentModule {}