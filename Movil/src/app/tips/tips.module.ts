import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { TipsPageRoutingModule } from './tips-routing.module';

import { TipsPage } from './tips.page';
import { ToolBarComponentModule } from '../components/tool-bar/tool-bar.module';
import { SlidesNoticiasPageModule } from 'app/slides-noticias/slides-noticias.module';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    TipsPageRoutingModule,
    ToolBarComponentModule,
    SlidesNoticiasPageModule
  ],
  declarations: [TipsPage]
})
export class TipsPageModule {}
