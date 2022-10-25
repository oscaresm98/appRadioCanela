import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { TipsPageRoutingModule } from './tips-routing.module';

import { TipsPage } from './tips.page';
import { PrincipalPageModule } from 'app/principal/principal.module';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    TipsPageRoutingModule,
    PrincipalPageModule
    
  ],
  declarations: [TipsPage]
})
export class TipsPageModule {}
