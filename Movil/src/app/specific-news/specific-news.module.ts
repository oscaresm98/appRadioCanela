import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { SpecificNewsPageRoutingModule } from './specific-news-routing.module';

import { SpecificNewsPage } from './specific-news.page';
import { BackToolbarComponentModule } from 'app/components/back-toolbar/back-toolbar.module';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    SpecificNewsPageRoutingModule,
    BackToolbarComponentModule
  ],
  declarations: [SpecificNewsPage]
})
export class SpecificNewsPageModule {}
