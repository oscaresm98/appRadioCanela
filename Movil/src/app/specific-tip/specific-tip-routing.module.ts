import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { SpecificTipPage } from './specific-tip.page';

const routes: Routes = [
  {
    path: '',
    component: SpecificTipPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class SpecificTipPageRoutingModule {}
