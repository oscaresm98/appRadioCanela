import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { StreamingAlternativePageRoutingModule } from './streaming-alternative-routing.module';

import { StreamingAlternativePage } from './streaming-alternative.page';

import { ToolBarComponentModule } from '../components/tool-bar/tool-bar.module';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    StreamingAlternativePageRoutingModule,
    ToolBarComponentModule
  ],
  declarations: [StreamingAlternativePage]
})
export class StreamingAlternativePageModule {}
