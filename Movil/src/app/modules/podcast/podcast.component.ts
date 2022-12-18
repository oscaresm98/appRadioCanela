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
  playlist: Array<Podcast> = [];

  player: Howl = null;
  activePodcast: Podcast = null;
  isPlaying: boolean = false;

  constructor(private backgroundService: ForegroundService, public podcastService: PodcastService) { }

  ngOnInit() {
    this.playlist=this.podcastService.getPodcast();
    console.log("Playlist: ",this.playlist);
  }

}

