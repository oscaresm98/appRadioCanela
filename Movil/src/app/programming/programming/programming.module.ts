import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { ProgrammingPageRoutingModule } from './programming-routing.module';

import { ProgrammingPage } from './programming.page';
import { BackToolbarComponentModule } from 'app/components/back-toolbar/back-toolbar.module';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    ProgrammingPageRoutingModule,
    BackToolbarComponentModule
  ],
  declarations: [ProgrammingPage]
})
export class ProgrammingPageModule {}
