import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { FutbolTeamPageRoutingModule } from './futbol-team-routing.module';

import { FutbolTeamPage } from './futbol-team.page';
import { BackToolbarComponentModule } from 'app/components/back-toolbar/back-toolbar.module';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    FutbolTeamPageRoutingModule,
    BackToolbarComponentModule
  ],
  declarations: [FutbolTeamPage]
})
export class FutbolTeamPageModule {}
