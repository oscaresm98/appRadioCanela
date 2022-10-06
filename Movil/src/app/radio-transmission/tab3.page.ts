import { AfterContentChecked, ChangeDetectorRef, Component, OnDestroy, OnInit, ViewChild} from '@angular/core';
import Swiper, { SwiperOptions, Pagination } from 'swiper';
import { SwiperComponent } from 'swiper/angular';

import { ActionPerformed, LocalNotifications } from '@capacitor/local-notifications';

import { StationService } from 'app/services/station.service';
import { Station } from 'app/shared/station';
import { Observable } from 'rxjs/internal/Observable';
import { RadioService } from 'app/services/radio.service';

Swiper.use([Pagination]);
@Component({
  selector: 'app-tab3',
  templateUrl: 'tab3.page.html',
  styleUrls: ['tab3.page.scss'],
})
export class Tab3Page implements OnInit, OnDestroy, AfterContentChecked {
  // Configuracion y componente deslizador
  @ViewChild('mySwiper') mySwiper: SwiperComponent;
  swiperConfig: SwiperOptions = { lazy: { checkInView:true }, pagination:true };

  // Arreglo y observable para manejar los datos de las emisoras
  stations$: Observable<Station[]>;
  stations: Station[] = [];

  // Emisora e indice actual
  currentStation: Station = { id:-1, name: 'Por defecto', dial: '', url:'', image:''};
  private currIndex = 0;

  constructor(
    private stationService: StationService,
    private changeDetector: ChangeDetectorRef,
    public radioService: RadioService
  ){}

  ngOnInit() {
    // Inicializamos la notificacion de que se esta escuchando la radio
    this.initializeNotificationRadio();

    // Obtenemos un observable para la informacion de las emisoras
    this.stations$ = this.stationService.getStationsInfo();

    // Seteamos todas las estaciones de radio para mostralo en slides
    this.stations$.subscribe(res => { this.stations = res as Station[]; });

    // Actualizamos la estacion de radio inicial
    this.setCurrentStation();
  }


  ngAfterContentChecked(): void {
    if(this.mySwiper){ this.mySwiper.updateSwiper({}); }
  }

  /**
   * Funcion que desactiva las notificaciones de esta pagina
   */
  async ngOnDestroy() {
    await LocalNotifications.deleteChannel({id:'channel_radio'});
  }

  /**
   * Actualiza la estacion de radio dependiendo del indice actual
   */
   async setCurrentStation() {
    const arrayOfStations = await this.stations$.toPromise();
    this.currentStation = arrayOfStations[this.currIndex];
    this.radioService.setRadioPlayer(this.currentStation);
    this.changeDetector.detectChanges();
  }


  /**
   * Funcion que se encarga de desactivar el reproductor cuando se haga un deslizamiento
   */
  async changeStation(event: any){
    this.radioService.pauseRadio();

    const elem: Swiper = event[0];
    this.currIndex = elem.activeIndex;

    // Eliminamos la notificacion de que se esta escuchando la radio
    LocalNotifications.cancel({ notifications:[{ id:1 }] });

    this.setCurrentStation();
  }

  stopRadioPlayer() {
    this.radioService.pauseRadio();
  }

  /**
   * Funcion que activa o desactiva el reproductor de radio
   *
   */
  playAudio(){
    if(!this.radioService.isPlaying){
      this.callNotification();
      this.radioService.playRadio();
    }
    else {
      // Eliminamos la notificacion de que se esta escuchando la radio
      LocalNotifications.cancel({ notifications:[{ id:1 }] });
      this.radioService.pauseRadio();
    }
  }

  /**
   * Funcion que carga una imagen por defecto
   */
  errorImage(event: any) {
    event.target.src = 'assets/images/Logo.png';
  }

  /**
   * Funcion que crea la notificacion y establece un oyente
   */
  async callNotification() {
    this.createNotification();
    LocalNotifications.addListener('localNotificationActionPerformed',
      (notification: ActionPerformed) => this.createNotification());
  }

  /**
   * Funcion para inicializar las notificaciones
   */
  private async initializeNotificationRadio() {
    await LocalNotifications.requestPermissions();

    // Creamos el canal para las notificaciones
    await LocalNotifications.createChannel({
      id:'channel_radio',
      sound: 'silent_quarter_second.wav',
      name: 'radio'
    });
  }

  /**
   * Funcion para crear una notificacion la cual indica que se esta escuchando la radio
   */
  private async createNotification() {
    await LocalNotifications.schedule({
      notifications:[{
        title:`${this.stations[this.currIndex].name}`,
        body:`Estas escuchando ${this.stations[this.currIndex].dial}`,
        id:1,
        ongoing:true,
        autoCancel:false,
        largeIcon: 'logo.png',
        channelId: 'channel_radio',
        sound: 'silent_quarter_second.wav'
      }]
    });
  }

}
