import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { ProfileEditPageRoutingModule } from './profile-edit-routing.module';

import { ProfileEditPage } from './profile-edit.page';
import { BackToolbarComponentModule } from 'app/components/back-toolbar/back-toolbar.module';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    ProfileEditPageRoutingModule,
    BackToolbarComponentModule
  ],
  declarations: [ProfileEditPage]
})
export class ProfileEditPageModule {}
