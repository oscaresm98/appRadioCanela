import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { TransmisionPageRoutingModule } from './transmision-routing.module';

import { TransmisionPage } from './transmision.page';
import { SwiperModule } from 'swiper/angular';
import { PrincipalPageModule } from 'app/principal/principal.module';
import { YouTubePlayerModule } from '@angular/youtube-player';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    SwiperModule,
    TransmisionPageRoutingModule,
    PrincipalPageModule,
    YouTubePlayerModule
  ],
  declarations: [TransmisionPage],
})
export class TransmisionPageModule {}
