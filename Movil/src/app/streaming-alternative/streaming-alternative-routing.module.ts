import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { StreamingAlternativePage } from './streaming-alternative.page';

const routes: Routes = [
  {
    path: '',
    component: StreamingAlternativePage
  },
  {
    path: ':id',
    loadChildren: () => import('../live-streaming/live-streaming.module').then(m => m.LiveStreamingPageModule)
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class StreamingAlternativePageRoutingModule {}
