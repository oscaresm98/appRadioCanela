import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ModulesRoutingModule } from './modules-routing.module';
import { IonicModule } from '@ionic/angular';
import { HomeComponent } from './home/home.component';
import { FormsModule } from '@angular/forms';
import { DialSubpageComponent } from './radio/components/dial-subpage/dial-subpage.component';
import { RadioComponent } from './radio/radio.component';
import { SwiperModule } from 'swiper/angular';
import { NoticiasComponent } from './noticias/noticias.component';
import { EquipoComponent } from './futbol/components/equipo/equipo.component';
import { MatchCardComponent } from './futbol/components/match-card/match-card.component';
import { PartidosComponent } from './futbol/components/partidos/partidos.component';
import { ModalFootbalComponent } from './futbol/components/modal-footbal/modal-footbal.component';
import { TipsComponent } from './tips/tips.component';
import { SpecificTipComponent } from './specific-tip/specific-tip.component';
import { SpecificNewComponent } from './noticias/components/specific-new/specific-new.component';
import { ProgramacionComponent } from './components/programacion/programacion.component';
import { TransmisionComponent } from './transmision/transmision.component';
import { GaleriaComponent } from './galeria/galeria.component';
import { PrincipalPageModule } from 'app/principal/principal.module';


@NgModule({
  declarations: [
    HomeComponent,
    DialSubpageComponent,
    RadioComponent,
    NoticiasComponent,
    EquipoComponent,
    MatchCardComponent,
    PartidosComponent,
    ModalFootbalComponent,
    TipsComponent,
    SpecificTipComponent,
    SpecificNewComponent,
    MatchCardComponent,
    ProgramacionComponent,
    TransmisionComponent,
    GaleriaComponent
  ],
  imports: [
    CommonModule,
    ModulesRoutingModule,
    IonicModule,
    FormsModule,
    SwiperModule,
    PrincipalPageModule
  ],
  exports:[
    ProgramacionComponent
  ]
})
export class ModulesModule { }
