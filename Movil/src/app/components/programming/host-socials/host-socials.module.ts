import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';
import { HostSocialsComponent } from './host-socials.component';

@NgModule({
  imports: [ CommonModule, FormsModule, IonicModule],
  declarations: [HostSocialsComponent],
  exports: [HostSocialsComponent]
})
export class HostSocialsComponentModule {}
