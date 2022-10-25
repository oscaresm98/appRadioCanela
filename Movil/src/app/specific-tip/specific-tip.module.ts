import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { SpecificTipPageRoutingModule } from './specific-tip-routing.module';

import { SpecificTipPage } from './specific-tip.page';
import { BackToolbarComponentModule } from 'app/components/back-toolbar/back-toolbar.module';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    SpecificTipPageRoutingModule,
    BackToolbarComponentModule
  ],
  declarations: [SpecificTipPage]
})
export class SpecificTipPageModule {}
