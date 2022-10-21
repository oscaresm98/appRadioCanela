import { IonicModule } from '@ionic/angular';
import { RouterModule } from '@angular/router';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Tab3Page } from './tab3.page';
import { ExploreContainerComponentModule } from '../explore-container/explore-container.module';

import { Tab3PageRoutingModule } from './tab3-routing.module';
import { ToolBarComponentModule } from '../components/tool-bar/tool-bar.module';

import { DialSubpageComponentModule } from '../components/radio/dial-subpage/dial-subpage.module';
import { SegmentRadioTableComponentModule } from '../components/radio/segment-radio-table/segment-radio-table.module';

import { SwiperModule } from 'swiper/angular';


@NgModule({
  imports: [
    IonicModule,
    CommonModule,
    FormsModule,
    ExploreContainerComponentModule,
    RouterModule.forChild([{ path: '', component: Tab3Page }]),
    Tab3PageRoutingModule,
    ToolBarComponentModule,
    DialSubpageComponentModule,
    SwiperModule,
    SegmentRadioTableComponentModule
  ],
  declarations: [Tab3Page]
})
export class Tab3PageModule {}
