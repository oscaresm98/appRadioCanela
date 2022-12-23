import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { EquipoComponent } from './futbol/components/equipo/equipo.component';
import { PartidosComponent } from './futbol/components/partidos/partidos.component';
import { HomeComponent } from './home/home.component';
import { InformacionComponent } from './informacion/informacion.component';
import { SpecificNewComponent } from './noticias/components/specific-new/specific-new.component';
import { NoticiasComponent } from './noticias/noticias.component';
import { RadioComponent } from './radio/radio.component';
import { TipsComponent } from './tips/tips.component';
import { SpecificTipComponent } from './specific-tip/specific-tip.component';
import { TransmisionComponent } from './transmision/transmision.component';
import { GaleriaComponent } from './galeria/galeria.component';
import { MyAccountComponent } from './my-account/my-account.component';
import { PodcastComponent } from './podcast/podcast.component';
import { ProgramaInfoComponent } from './programa-info/programa-info.component';
import { LocutorInfoComponent } from './locutor-info/locutor-info.component';

const routes: Routes = [
  {
    path: '',
    data: { breadcrumb: 'Principal' },
    children: [
      {
        path: '',
        pathMatch: 'full',
        redirectTo: 'home',
      },
      {
        path: 'home',
        component: HomeComponent
      },
      {
        path: 'radio',
        component: RadioComponent
      },
      {
        path: 'informacion',
        component: InformacionComponent
      },
      {
        path: 'noticias',
        component: NoticiasComponent
      },
      {
        path: 'noticias/:id',
        component: SpecificNewComponent
      },
      {
        path: 'partidos',
        component: PartidosComponent
      },
      {
        path: 'equipo/:id',
        component: EquipoComponent
      },
      {
        path: 'tips',
        component: TipsComponent
      },
      {
        path: 'tips/:id',
        component: SpecificTipComponent
      },
      {
        path: 'transmision',
        component: TransmisionComponent
      },
      {
        path: 'galeria',
        component: GaleriaComponent
      },
      {
        path: 'my-account',
        component: MyAccountComponent
      },
      {
        path: 'podcast',
        component: PodcastComponent
      },
      {
        path: 'programa-info/:id',
        component: ProgramaInfoComponent
      },
      {
        path: 'locutor-info/:idPrograma/:idLocutor',
        component: LocutorInfoComponent
      },

    ]
    }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ModulesRoutingModule { }
