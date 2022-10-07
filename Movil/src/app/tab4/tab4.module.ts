import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { Tab4PageRoutingModule } from './tab4-routing.module';

import { Tab4Page } from './tab4.page';
import { ExploreContainerComponentModule } from 'app/explore-container/explore-container.module';
import { ToolBarComponentModule } from 'app/components/tool-bar/tool-bar.module';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    Tab4PageRoutingModule,
    ExploreContainerComponentModule,
    ToolBarComponentModule,
  ],
  declarations: [Tab4Page]
})
export class Tab4PageModule {}
