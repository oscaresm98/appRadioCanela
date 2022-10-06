import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { FutbolTeamPage } from './futbol-team.page';

const routes: Routes = [
  {
    path: '',
    component: FutbolTeamPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class FutbolTeamPageRoutingModule {}
