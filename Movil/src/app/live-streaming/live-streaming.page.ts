/* eslint-disable radix */
import { Component, OnInit } from '@angular/core';
import { DomSanitizer } from '@angular/platform-browser';
import { ActivatedRoute } from '@angular/router';
import { StreamingService } from 'app/services/streaming.service';
import { Streaming } from 'app/shared/streaming';

@Component({
  selector: 'app-live-streaming',
  templateUrl: './live-streaming.page.html',
  styleUrls: ['./live-streaming.page.scss'],
})
export class LiveStreamingPage implements OnInit {

  idStream: any;
  streamInfo: Streaming;

  constructor( private streamService: StreamingService, private activeRouter: ActivatedRoute, private dom: DomSanitizer) {}

  ngOnInit() {
    const id = this.activeRouter.snapshot.paramMap.get('id');

    const i = this.streamService.getStreamById(parseInt(id));

    console.log(i);
    this.streamInfo = i;
  }

  getUrl(url: string) {
    const newUrl = this.dom.bypassSecurityTrustResourceUrl(url);
    return newUrl;
  }

}
