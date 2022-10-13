import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { SlidesNoticiasPageRoutingModule } from './slides-noticias-routing.module';

import { SlidesNoticiasPage } from './slides-noticias.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    SlidesNoticiasPageRoutingModule
  ],
  declarations: [SlidesNoticiasPage],
  exports:[
    SlidesNoticiasPage
  ]
})
export class SlidesNoticiasPageModule {}