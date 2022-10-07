import { ChangeDetectorRef, Component, OnDestroy, OnInit } from '@angular/core';
import { DomSanitizer } from '@angular/platform-browser';
import { StreamingService } from 'app/services/streaming.service';
import { Streaming } from 'app/shared/streaming';
import Swiper, { Navigation } from 'swiper';
import { SwiperOptions } from 'swiper/types/swiper-options';

Swiper.use([Navigation]);
@Component({
  selector: 'app-tab2',
  templateUrl: 'tab2.page.html',
  styleUrls: ['tab2.page.scss']
})
export class Tab2Page implements OnInit, OnDestroy {
  swiperConfig: SwiperOptions = { lazy: { checkInView:true }, navigation: true };

  platforms: string[];

  streamings: Streaming[];

  currentStream: Streaming;

  private currIndex = 0;

  constructor(private liveStreamService: StreamingService,  private changeDetector: ChangeDetectorRef, private dom: DomSanitizer) {}

  ngOnInit(): void {
    this.streamings = this.liveStreamService.getStreamings();
    this.platforms = this.streamings.map(stream => stream.platform);
    this.currentStream = this.streamings[this.currIndex];
  }

  ngOnDestroy(): void {
    // throw new Error('Method not implemented.');
  }

  async changePlatform(event: any) {
    const elem: Swiper = event[0];
    this.currIndex = elem.activeIndex;
    this.currentStream = this.streamings[this.currIndex];
    this.changeDetector.detectChanges();
    console.log(this.currIndex);
    console.log(this.currentStream);
  }

  sanatize(iframeStr: string) {
    return this.dom.bypassSecurityTrustResourceUrl(iframeStr);
  }

  putIframe(iframeStr: string) {
    return this.dom.bypassSecurityTrustHtml(iframeStr);
  }

}
