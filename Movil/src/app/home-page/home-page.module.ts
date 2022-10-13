import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { HomePagePageRoutingModule } from './home-page-routing.module';

import { HomePagePage } from './home-page.page';
import { ToolBarComponentModule } from '../components/tool-bar/tool-bar.module';
import { SlidesNoticiasPageModule } from 'app/slides-noticias/slides-noticias.module';


@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    HomePagePageRoutingModule,
    ToolBarComponentModule,
    SlidesNoticiasPageModule
  ],
  declarations: [HomePagePage]
})
export class HomePagePageModule {}
