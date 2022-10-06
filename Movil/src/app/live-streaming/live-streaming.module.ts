import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { LiveStreamingPageRoutingModule } from './live-streaming-routing.module';

import { LiveStreamingPage } from './live-streaming.page';

import { BackToolbarComponentModule } from '../components/back-toolbar/back-toolbar.module';
import { CarouselComponentModule } from '../components/carousel/carousel.module';


@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    LiveStreamingPageRoutingModule,
    BackToolbarComponentModule,
    CarouselComponentModule
  ],
  declarations: [
    LiveStreamingPage,
  ]
})
export class LiveStreamingPageModule {}
