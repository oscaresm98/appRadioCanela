import { AfterContentChecked, ChangeDetectorRef, Component, OnInit, QueryList, ViewChild, ViewChildren } from '@angular/core';
import { AlertController, LoadingController } from '@ionic/angular';
import { RadioService } from 'app/services/radio/radio.player.service';
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
  //@ViewChildren('radioStation') radioStations: QueryList<DialSubpageComponent>;

  swiperConfig: SwiperOptions = { 
    lazy: { checkInView: true }, 
    pagination: false ,
    spaceBetween:-120};

  // Arreglo y observable para manejar los datos de las emisoras
  stations: Station[] = [];

  // Emisora e indice actual
  currentStation: Station;
  private currIndex = 0;

  constructor(
    private stationService: StationService,
    private changeDetector: ChangeDetectorRef,
    private loadingCtrl: LoadingController,
    public radioService: RadioService,
    private alertCtrl: AlertController
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

    //this.radioStations.get(elem.previousIndex).destroyRadio();


    this.currIndex = elem.activeIndex;
    console.log("EVENTO SWIPER: ",event)
    this.currentStation = this.stations[this.currIndex];
    console.log("Nueva station---:",this.currentStation)
    this.destroyRadio();
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
  // Emisora methods
  isPlaying = false;
  
  playPauseRadio() {
    if(!this.radioService.radioPlayer) {
      this.showLoading(); // Mostramos la senal de cargando
      this.radioService.setRadioPlayer(
        this.currentStation.url_streaming,
        () => this.loadingCtrl.dismiss(),
        () => {
          this.showAlert(); // Mostramos una alerta
          this.isPlaying = false;
          this.radioService.radioPlayer = undefined;
        }
      );
    }

    if(!this.isPlaying) {
      this.radioService.playRadio(this.currentStation.frecuencia_dial);
      this.isPlaying = true;
    }
    else {
      this.radioService.pauseRadio();
      this.isPlaying = false;
    }

  }

  /**
   * Mostrar ventana emegente de cargando cuando se inicia la radio
   */
  async showLoading() {
    const load = await this.loadingCtrl.create({
      message: 'Cargando...',
      spinner:'bubbles',
    });
    load.present();
  }

  /**
   * Mostrar alerta cuando hay un error al cargar la radio
   */
  async showAlert() {
    const alert = await this.alertCtrl.create({
      message: 'Error al cargar la transmision. Por favor intentelo mas tarde',
      buttons: ['OK'],
      mode: 'ios'
    });
    alert.present();
  }

  destroyRadio() {
    this.isPlaying = false;
    this.radioService.destroyRadio();
  }
}
