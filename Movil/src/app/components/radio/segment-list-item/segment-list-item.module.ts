import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';
import { SegmentListItemComponent } from './segment-list-item.component';

@NgModule({
  imports: [ CommonModule, FormsModule, IonicModule],
  declarations: [SegmentListItemComponent],
  exports: [SegmentListItemComponent]
})
export class SegmentListItemModule { }
