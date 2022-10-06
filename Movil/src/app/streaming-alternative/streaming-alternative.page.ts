import { Component, OnDestroy, OnInit } from '@angular/core';
import { StreamingService } from 'app/services/streaming.service';

@Component({
  selector: 'app-streaming-alternative',
  templateUrl: './streaming-alternative.page.html',
  styleUrls: ['./streaming-alternative.page.scss'],
})
export class StreamingAlternativePage implements OnInit, OnDestroy {

  streamings: any[] = [];

  constructor(private liveStreamService: StreamingService) {}

  ngOnInit(): void {
    this.streamings = this.liveStreamService.getStreamings();
  }

  ngOnDestroy(): void {
    // throw new Error('Method not implemented.');
  }


}
