import { IonicModule } from '@ionic/angular';
import { RouterModule } from '@angular/router';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Tab2Page } from './tab2.page';
import { ExploreContainerComponentModule } from '../explore-container/explore-container.module';

import { Tab2PageRoutingModule } from './tab2-routing.module';
import { ToolBarComponentModule } from '../components/tool-bar/tool-bar.module';
import { SwiperModule } from 'swiper/angular';
import { CarouselComponentModule } from 'app/components/carousel/carousel.module';

@NgModule({
  imports: [
    IonicModule,
    CommonModule,
    FormsModule,
    ExploreContainerComponentModule,
    Tab2PageRoutingModule,
    ToolBarComponentModule,
    SwiperModule,
    CarouselComponentModule
  ],
  declarations: [Tab2Page]
})
export class Tab2PageModule {}
