import { Component, OnInit } from '@angular/core';
import { ForegroundService } from '@awesome-cordova-plugins/foreground-service/ngx';
import { PodcastService } from 'app/services/podcast/podcast.service';
import { Podcast } from 'app/shared/podcast';
import { Howl } from 'howler';

@Component({
  selector: 'app-podcast-menu',
  templateUrl: './podcast.component.html',
  styleUrls: ['./podcast.component.scss'],
})
export class PodcastComponent implements OnInit {
  listo: boolean = true;
  allplaylist: any = [];
  ourPlaylist: any = [];
  date: string = '';
  months = ['en.', 'febr.', 'mzo.', 'abr.','may.', 'jun.', 'jul.', 'agt.','sept.', 'oct.', 'nov.', 'dic.']

  player: Howl = null;
  activePodcast: any = null;
  isPlaying: boolean = false;
  progress: number = 0;
  

  

  constructor(private backgroundService: ForegroundService, public podcastService: PodcastService) { }

  ngOnInit() {
    this.podcastService.getAllPodcast().subscribe(e => {
      //console.log("Servicio: ",e);
      this.allplaylist = e;
      for (let i=0; i<this.allplaylist.length;i++){
        this.ourPlaylist.push(this.allplaylist.pop());
      }
    })

    console.log("Esta es nuestra: ",this.ourPlaylist);
  }

  public start (podcast:Podcast) {
    this.activePodcast=podcast;
    console.log("Active podcast", this.activePodcast);
    console.log("Podcast ",podcast);
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
    let index = this.ourPlaylist. indexOf(this.activePodcast)
    if (index != this.ourPlaylist.length - 1) {
      this.start(this.ourPlaylist[index+1])
    } else {
      this.start(this.ourPlaylist[0])
    }
  }

  /**
   * 
   */
  public prev() {
    let index = this.ourPlaylist. indexOf(this.activePodcast)
    if (index > 1) {
      this.start(this.ourPlaylist[index-1])
    } else {
      this.start(this.ourPlaylist[this.ourPlaylist.length-1])
    }
  }

  public seek() {
    let newValue = +this.podcastService.range.value;
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

