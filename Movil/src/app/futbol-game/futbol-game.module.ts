import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { FutbolGamePageRoutingModule } from './futbol-game-routing.module';

import { FutbolGamePage } from './futbol-game.page';
import { BackToolbarComponentModule } from 'app/components/back-toolbar/back-toolbar.module';
import { MatchCardComponentModule } from 'app/components/football/match-card/match-card.module';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    FutbolGamePageRoutingModule,
    BackToolbarComponentModule,
    MatchCardComponentModule
  ],
  declarations: [FutbolGamePage]
})
export class FutbolGamePageModule {}
