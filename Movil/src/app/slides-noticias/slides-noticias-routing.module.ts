import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { SlidesNoticiasPage } from './slides-noticias.page';

const routes: Routes = [
  {
    path: '',
    component: SlidesNoticiasPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class SlidesNoticiasPageRoutingModule {}
