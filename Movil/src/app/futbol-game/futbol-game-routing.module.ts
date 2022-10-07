import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { FutbolGamePage } from './futbol-game.page';

const routes: Routes = [
  {
    path: '',
    component: FutbolGamePage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class FutbolGamePageRoutingModule {}
