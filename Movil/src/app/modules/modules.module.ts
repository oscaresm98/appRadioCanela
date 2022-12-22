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
import { BannerComponent } from './components/banner/banner.component';
import { SlidesComponent } from './components/slides/slides.component';
import { NoticiaCardComponent } from './noticias/components/noticia-card/noticia-card.component';
import { MyAccountComponent } from './my-account/my-account.component';
import { PodcastComponent} from './podcast/podcast.component';
import {PodcastBarComponent} from './podcast/component/podcast-bar/podcast-bar.component';
import {PodcastInfoComponent} from './podcast/component/podcast-info/podcast-info.component';
import {PlayerComponent} from './podcast/component/player/player.component';
import { FooterComponent } from './components/footer/footer.component';
import { ProgramaInfoComponent } from './programa-info/programa-info.component';
import { LocutorInfoComponent } from './locutor-info/locutor-info.component';
import { InformacionComponent } from './informacion/informacion.component';


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
    GaleriaComponent,
    BannerComponent,
    SlidesComponent,
    NoticiaCardComponent,
    MyAccountComponent,
    PodcastComponent,
    PodcastBarComponent,
    PodcastInfoComponent,
    PlayerComponent,
    FooterComponent,
    ProgramaInfoComponent,
    LocutorInfoComponent,
    InformacionComponent
    
  ],
  imports: [
    CommonModule,
    ModulesRoutingModule,
    IonicModule,
    FormsModule,
    SwiperModule,
  ],
  exports:[
    ProgramacionComponent
  ]
})
export class ModulesModule { }
