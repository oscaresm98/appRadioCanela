import { ChangeDetectorRef, Component, ElementRef, OnDestroy, OnInit, ViewChild } from '@angular/core';
import { DomSanitizer } from '@angular/platform-browser';
import { StreamingService } from 'app/services/streaming.service';
import { Streaming } from 'app/shared/streaming';
import { getUrlFacebookVideo } from 'app/shared/utils';
import Swiper, { Navigation, SwiperOptions } from 'swiper';

Swiper.use([Navigation]);
@Component({
  selector: 'app-transmision',
  templateUrl: './transmision.page.html',
  styleUrls: ['./transmision.page.scss'],
})
export class TransmisionPage implements OnInit, OnDestroy {
  @ViewChild('loadingDiv') loadingDiv: ElementRef;
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

  getUrlVideo(url: string, platform: string) {
    let newUrl = '';

    switch (platform.toLowerCase()) {
      case 'facebook':
        newUrl = getUrlFacebookVideo(url);
        break;
      default:
        break;
    }
    return this.dom.bypassSecurityTrustResourceUrl(newUrl);
  }

  onLoadStream() {
    // console.log(this.loading.nativeElement.classList);
    this.loadingDiv.nativeElement.style.display = 'none';
  }

}
