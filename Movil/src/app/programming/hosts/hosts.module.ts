import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { HostsPageRoutingModule } from './hosts-routing.module';

import { HostsPage } from './hosts.page';
import { BackToolbarComponentModule } from 'app/components/back-toolbar/back-toolbar.module';
import { HostSocialsComponentModule } from 'app/components/programming/host-socials/host-socials.module';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    HostsPageRoutingModule,
    BackToolbarComponentModule,
    HostSocialsComponentModule
  ],
  declarations: [HostsPage]
})
export class HostsPageModule {}
