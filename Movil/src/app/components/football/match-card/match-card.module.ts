import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { IonicModule } from '@ionic/angular';

import { MatchCardComponent } from './match-card.component';



@NgModule({
  declarations: [MatchCardComponent],
  exports: [MatchCardComponent],
  imports: [CommonModule, IonicModule]
})
export class MatchCardComponentModule { }
