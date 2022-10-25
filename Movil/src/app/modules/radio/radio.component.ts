import { AfterContentChecked, ChangeDetectorRef, Component, OnInit, QueryList, ViewChild, ViewChildren } from '@angular/core';
import { LoadingController } from '@ionic/angular';
import { StationService } from 'app/services/radio/station.service';

import { Station } from 'app/shared/station';
import Swiper, { SwiperOptions } from 'swiper';
import { SwiperComponent } from 'swiper/angular';
import { DialSubpageComponent } from './components/dial-subpage/dial-subpage.component';

@Component({
  selector: 'app-radio',
  templateUrl: './radio.component.html',
  styleUrls: ['./radio.component.scss'],
})
export class RadioComponent implements OnInit, AfterContentChecked {
  // Configuracion y componente deslizador
  @ViewChild('mySwiper') mySwiper: SwiperComponent;
  @ViewChildren('radioStation') radioStations: QueryList<DialSubpageComponent>;

  swiperConfig: SwiperOptions = { 
    lazy: { checkInView: true }, 
    pagination: false ,
    spaceBetween:-100};

  // Arreglo y observable para manejar los datos de las emisoras
  stations: Station[] = [];

  // Emisora e indice actual
  currentStation: Station = { id: -1, radio: null, frecuencia_dial: '', url_streaming: '' };
  private currIndex = 0;

  constructor(
    private stationService: StationService,
    private changeDetector: ChangeDetectorRef,
    private loadingCtrl: LoadingController
  ) { }

  async ngOnInit() {
    const loading = await this.showLoadingData();

    this.stationService.getStationsInfo().subscribe(
      resp => {
        this.stations = resp as Station[];
        this.currentStation = this.stations[0];
        console.log("---Lsit: ", this.stations)
        console.log("----CURRENT STATION: ", this.currentStation)
        loading.dismiss();
      },
      error => loading.dismiss()
    );

    this.loadingCtrl.dismiss();
  }


  ngAfterContentChecked(): void {
    if (this.mySwiper) { this.mySwiper.updateSwiper({}); }
  }

  /**
   * Funcion que se encarga de desactivar el reproductor cuando se haga un deslizamiento
   */
  async changeStation(event: any) {
    const elem: Swiper = event[0];

    this.radioStations.get(elem.previousIndex).destroyRadio();

    this.currIndex = elem.activeIndex;

    this.currentStation = this.radioStations.get(this.currIndex).station;
    this.changeDetector.detectChanges();
  }

  /**
   * Funcion que carga una imagen por defecto
   */
  errorImage(event: any) {
    event.target.src = 'assets/images/Logo.png';
  }

  private async showLoadingData() {
    const loadingModal = await this.loadingCtrl.create({
      message: 'Cargando Emisoras',
      mode: 'ios',
      spinner: 'circular'
    });

    await loadingModal.present();
    return loadingModal;
  }
}
