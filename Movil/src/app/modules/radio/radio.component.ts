import { AfterContentChecked, ChangeDetectorRef, Component, OnInit, QueryList, ViewChild, ViewChildren } from '@angular/core';
import { AlertController, LoadingController } from '@ionic/angular';
import { AlertService } from 'app/services/alert.service';
import { DataService } from 'app/services/data/data.service';
import { RadioService } from 'app/services/radio/radio.player.service';
import { StationService } from 'app/services/radio/station.service';
import { ProgramPerDia } from 'app/shared/program';

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
    spaceBetween:-170};

  // Arreglo y observable para manejar los datos de las emisoras
  stations: Station[] = [];

  // Emisora e indice actual
  currentStation: Station;
   currIndex = 0;

  //programacion
  programacionesAllRadios: ProgramPerDia[][]=[];
  currentProgramacion:ProgramPerDia[]=[];
  //likes
  isLiking:boolean[]=[];

  constructor(
    private stationService: StationService,
    private changeDetector: ChangeDetectorRef,
    private loadingCtrl: LoadingController,
    public radioService: RadioService,
    private alertCtrl: AlertController,
    private dataService: DataService,
    private alertService: AlertService
  ) { }

  async ngOnInit() {
    const loading = await this.showLoadingData();
    this.stationService.getEmisoras().then(
      async (data:any)=>{
        if (data.resCode == 0) {
          this.stations=data.resData;
          this.currentStation = this.stations[0];
        await this.getAllProgramsRadio();
        this.currentProgramacion=this.programacionesAllRadios[0];
        this.fillLikesList(this.stations.length);
        loading.dismiss();
        } else {
          this.alertService.displayErrorMessage('Error al cargar las emisoras.')
        }
      }
    )
    
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
    this.currentProgramacion=this.programacionesAllRadios[this.currIndex];
    this.destroyRadio();
    this.changeDetector.detectChanges();
  }
  like(){
    const index=this.currIndex;
    this.isLiking[index]=!this.isLiking[index];
  }
  hasPrevious(){
    if(this.currIndex==0) return false;
    return true
  }
  hasNext(){
    if(this.currIndex==this.stations.length-1) return false;
    return true
  }
  getLeft(){
    if(this.currentStation==null) return '';
    else if(this.currIndex==0) return this.currentStation.frecuencia_dial;
    return this.stations[this.currIndex-1].ciudad;
  }
  getRigth(){
    if(this.currentStation==null) return '';
    else if(this.currIndex==this.stations.length-1) return this.currentStation.frecuencia_dial;
    return this.stations[this.currIndex+1].ciudad;
  }
  hourFormat(hora:string){
    let list=hora.split(":")
    return list[0]+':'+list[1];
  }
  getOnLiveProgramName(){
    if(this.currentProgramacion==null) return "default";
    if(this.currentProgramacion.length<1) return "default";
    const programa=this.getProgramaOnLive(this.currentProgramacion);
    return programa.programa[0].nombre;
  }
  getOnLiveProgramHour(){
    if(this.currentProgramacion==null) return "00:00";
    if(this.currentProgramacion.length<1) return "00:00";
    const programa=this.getProgramaOnLive(this.currentProgramacion);
    return this.hourFormat(programa.hora_inicio)+" - "+
      this.hourFormat(programa.hora_fin);
  }
  getOnLiveProgramImage(index:number){
    if(this.programacionesAllRadios==null) return "assets/images/cantera.jpg";
    if(this.programacionesAllRadios.length<1) return "assets/images/cantera.jpg";
    console.log("LISTA PROGRAMACIONES: ",this.programacionesAllRadios)
    const programa=this.getProgramaOnLive(this.programacionesAllRadios[index]);
    return programa.programa[0].imagen;
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
  private async getAllProgramsRadio(){
    for( let emisora of this.stations){
      await this.getProgramaRadio(emisora);
    }
  }
  private async getProgramaRadio(emisora: Station){
    const loading=this.showLoadingData();
    const today=this.getToday();
    //const idEmisora=this.currentStation.id;
    await this.dataService.getProgramaRadioPerDay(emisora.id,today).then(
      (data:any)=>{
        if (data.resCode == 0) {
          //this.programacion=data.resData;
          this.programacionesAllRadios.push(data.resData)
          console.log("Id: ",emisora.id," ",today)
          console.log("Raadio: ",emisora.ciudad," ",data.resData)
        } else {
          console.log("ERROR AL OBTEBER NOCTICIAS")
        }
        this.loadingCtrl.dismiss();
      }
      );
  }
  private getToday(){
    const date:Date=new Date();
    switch(date.getDay()){
      case 1:
        return 'Lunes';
      case 2:
        return 'Martes';
      case 3:
        return 'Miércoles'
      case 4:
        return 'Jueves';
      case 5:
        return 'Viernes';
      case 6:
        return 'Sábado';
      case 7:
        return 'Domingo';
    }
  }
  private fillLikesList(len:number){
    for(let i=0;i<len;i++){
      this.isLiking.push(false);
    }
  }
   private getProgramaOnLive(listaProgramacion:ProgramPerDia[]){
    const date=new Date();
    const time=date.getHours()+":"+date.getMinutes()
    const programa=listaProgramacion.find(programa=>this.hourFormat(programa.hora_inicio)<=time 
    && this.hourFormat(programa.hora_fin)>=time)
    if(programa==null) return listaProgramacion[0];
    return programa;
  }
}