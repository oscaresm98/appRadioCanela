import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';
import { ToolBarComponent } from './tool-bar.component';
import { ToolBarComponentRoutingModule } from './tool-bar-routing.module';

@NgModule({
  imports: [ CommonModule, FormsModule, IonicModule, ToolBarComponentRoutingModule],
  declarations: [ToolBarComponent],
  exports: [ToolBarComponent]
})
export class ToolBarComponentModule {}
