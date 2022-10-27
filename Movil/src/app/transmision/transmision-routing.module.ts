import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { TransmisionPage } from './transmision.page';

const routes: Routes = [
  {
    path: '',
    component: TransmisionPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class TransmisionPageRoutingModule {}
