import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { NewsPageRoutingModule } from './news-routing.module';

import { NewsPage } from './news.page';
import { BackToolbarComponentModule } from 'app/components/back-toolbar/back-toolbar.module';
import { SocialSharing } from '@awesome-cordova-plugins/social-sharing/ngx';
@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    NewsPageRoutingModule,
    BackToolbarComponentModule
  ],
  declarations: [NewsPage],
  providers:[SocialSharing]
})
export class NewsPageModule {}
