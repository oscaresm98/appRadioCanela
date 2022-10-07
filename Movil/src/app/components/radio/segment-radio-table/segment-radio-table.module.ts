import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';
import { SegmentRadioTableComponent } from './segment-radio-table.component';
import { SegmentListItemModule } from '../segment-list-item/segment-list-item.module';

@NgModule({
  imports: [ CommonModule, FormsModule, IonicModule, SegmentListItemModule],
  declarations: [SegmentRadioTableComponent],
  exports: [SegmentRadioTableComponent]
})
export class SegmentRadioTableComponentModule {}
