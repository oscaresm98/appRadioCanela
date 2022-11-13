import { Injectable, ViewChild } from '@angular/core';
import { ForegroundService } from '@awesome-cordova-plugins/foreground-service/ngx';
import { IonRange } from '@ionic/angular';
import { Podcast } from 'app/shared/podcast';
import { Howl } from 'howler';
import { StopRadioService } from '../stop-radio.service';

@Injectable({
  providedIn: 'root'
})

export class PodcastService {

  playlist: Array<Podcast> = [];
  player: Howl = null;
  activePodcast: Podcast = null;
  isPlaying: boolean = false;
  progress: number = 0;
  date: string = '';
  months = ['en.', 'febr.', 'mzo.', 'abr.','may.', 'jun.', 'jul.', 'agt.','sept.', 'oct.', 'nov.', 'dic.']

  @ViewChild('range', { static : false}) 
  range: IonRange;

  constructor(private backgroundService: ForegroundService,/* private stopRadio:StopRadioService*/) { }

  public getPodcast() {
    this.playlist = [
      {
        id:1 ,
        nombre: "All that",
        descripcion:" Cancion sin copyright, con duración de 2 min que sirve principalmente para pruebas de desarrollo de app movil de la radio canela",
        audio: '../../../assets/sounds/allthat.mp3',
        fecha: '2022-05-14',
        imagen: 'https://images.squarespace-cdn.com/content/v1/5d2e2c5ef24531000113c2a4/1564770289250-9FPM7TAI5O56U9JQTPVO/album-placeholder.png?format=1000w',
        autores: 'Radio Canela',
        likes: 3
      },
      {
        id:2,
        nombre: "Creative minds",
        descripcion:"",
        audio: '../../../assets/sounds/creativeminds.mp3',
        fecha: '2022-05-14',
        imagen: 'https://images.squarespace-cdn.com/content/v1/5d2e2c5ef24531000113c2a4/1564770289250-9FPM7TAI5O56U9JQTPVO/album-placeholder.png?format=1000w',
        autores: 'Radio Canela',
        likes: 3
      },
      {
        id:3,
        nombre: "Dreams",
        descripcion:"",
        audio: '../../../assets/sounds/dreams.mp3',
        fecha: '2022-05-14',
        imagen: 'https://images.squarespace-cdn.com/content/v1/5d2e2c5ef24531000113c2a4/1564770289250-9FPM7TAI5O56U9JQTPVO/album-placeholder.png?format=1000w',
        autores: 'Radio Canela',
        likes: 3
      },
      {
        id:1 ,
        nombre: "All that",
        descripcion:" Cancion sin copyright, con duración de 2 min que sirve principalmente para pruebas de desarrollo de app movil de la radio canela",
        audio: '../../../assets/sounds/allthat.mp3',
        fecha: '2022-05-14',
        imagen: 'https://images.squarespace-cdn.com/content/v1/5d2e2c5ef24531000113c2a4/1564770289250-9FPM7TAI5O56U9JQTPVO/album-placeholder.png?format=1000w',
        autores: 'Radio Canela',
        likes: 3
      },
      {
        id:2,
        nombre: "Creative minds",
        descripcion:"",
        audio: '../../../assets/sounds/creativeminds.mp3',
        fecha: '2022-05-14',
        imagen: 'https://images.squarespace-cdn.com/content/v1/5d2e2c5ef24531000113c2a4/1564770289250-9FPM7TAI5O56U9JQTPVO/album-placeholder.png?format=1000w',
        autores: 'Radio Canela',
        likes: 3
      },
      {
        id:3,
        nombre: "Dreams",
        descripcion:"",
        audio: '../../../assets/sounds/dreams.mp3',
        fecha: '2022-05-14',
        imagen: 'https://images.squarespace-cdn.com/content/v1/5d2e2c5ef24531000113c2a4/1564770289250-9FPM7TAI5O56U9JQTPVO/album-placeholder.png?format=1000w',
        autores: 'Radio Canela',
        likes: 3
      }
    ]

    return this.playlist;
  }

  public start (podcast:Podcast) {
    if (this.player){
      this.player.stop();
      /* this.backgroundService.stop(); */
    }
    this.player = new Howl({
      src:[podcast.audio],
      onplay: () => {
        this.isPlaying = true;
        this.activePodcast = podcast;
        this.formatDate(podcast);
        this.updateProgress();
        /* this.stopRadio.stopRadio(); */
      },
      onend: () => {
        this.next();
      }
    })
    this.player.play()
    /*this.backgroundService.start('App Radio Forever', `Estas escuchando ${dial}`, 'drawable/fsicon');*/
    /* this.backgroundService.start('App Radio Forever', `Estas escuchando ${podcast.nombre}`, 'drawable/fsicon'); */
  }

  public togglePlayer(pause) {
    this.isPlaying = !pause;
    if (pause) {
      this.player.pause();
    } else {
      this.player.play();
    }
  }

  public next() {
    let index = this.playlist. indexOf(this.activePodcast)
    if (index != this.playlist.length - 1) {
      this.start(this.playlist[index+1])
    } else {
      this.start(this.playlist[0])
    }
  }

  /**
   * 
   */
  public prev() {
    let index = this.playlist. indexOf(this.activePodcast)
    if (index > 1) {
      this.start(this.playlist[index-1])
    } else {
      this.start(this.playlist[this.playlist.length-1])
    }
  }

  public seek() {
    let newValue = +this.range.value;
    let duration = this.player.duration();
    this.player.seek(duration * (newValue/100));
  }

  public updateProgress(){
    let seek = this.player.seek();
    this.progress = (seek / this.player.duration()) * 100 || 0;
    setTimeout(() => {
      this.updateProgress();
    }, 1000)
  }

  public formatDate(podcast:Podcast){
    let tempDate = new Date(podcast.fecha)
    this.date = tempDate.getDay() + ' ' + this.months[tempDate.getMonth()]
  }
}
