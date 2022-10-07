import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';
import { BackToolbarComponent } from './back-toolbar.component';

@NgModule({
  imports: [ CommonModule, FormsModule, IonicModule],
  declarations: [BackToolbarComponent],
  exports: [BackToolbarComponent]
})
export class BackToolbarComponentModule {}
