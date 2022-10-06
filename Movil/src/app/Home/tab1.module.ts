import { IonicModule } from '@ionic/angular';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Tab1Page } from './tab1.page';
import { ExploreContainerComponentModule } from '../explore-container/explore-container.module';

import { Tab1PageRoutingModule } from './tab1-routing.module';
import { ToolBarComponent } from '../components/tool-bar/tool-bar.component';
import { ToolBarComponentModule } from '../components/tool-bar/tool-bar.module';
import { CarouselComponentModule } from '../components/carousel/carousel.module';
import { BackToolbarComponentModule } from 'app/components/back-toolbar/back-toolbar.module';

@NgModule({
  imports: [
    IonicModule,
    CommonModule,
    FormsModule,
    ExploreContainerComponentModule,
    Tab1PageRoutingModule,
    ToolBarComponentModule,
    CarouselComponentModule,
    BackToolbarComponentModule
  ],
  declarations: [Tab1Page]
})
export class Tab1PageModule {}
