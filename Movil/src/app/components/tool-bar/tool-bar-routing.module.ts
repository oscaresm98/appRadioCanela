import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ToolBarComponent } from './tool-bar.component';

const routes: Routes = [
  {
    path: '',
    component: ToolBarComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class ToolBarComponentRoutingModule {}