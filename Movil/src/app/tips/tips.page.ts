import { Component, OnInit, ViewChild } from '@angular/core';
import { SocialSharing } from '@awesome-cordova-plugins/social-sharing/ngx';
import { IonInfiniteScroll } from '@ionic/angular';
import { DataService } from 'app/services/data/data.service';

@Component({
  selector: 'app-tips',
  templateUrl: './tips.page.html',
  styleUrls: ['./tips.page.scss'],
})
export class TipsPage implements OnInit {

  @ViewChild(IonInfiniteScroll, { static: true }) infiniteScroll: IonInfiniteScroll;
  allTipsList: any = [];
  tipsList: any = [];
  allTLength;
  constructor(private socialSharing: SocialSharing, private data: DataService) { }

  ngOnInit() {
    this.data.getTips().subscribe(e => {
      this.allTipsList = e;
      this.allTLength = this.allTipsList.length;
      for (let i = 0; i < this.allTLength && i < 10; i++) {
        this.tipsList.push(this.allTipsList.pop());
      }
    });
  }

  public interactionMaganer(interactions: number) {
    let interactionsText;
    if (interactions <= 1000) {
      interactionsText = interactions.toString();
    }
    if (interactions >= 1000) {
      const temp = Math.round(interactions / 1000);
      interactionsText = temp + 'k';
    }
    if (interactions >= 1000000) {
      const temp = Math.round(interactions / 1000000);
      interactionsText = temp + 'mill';
    }

    return interactionsText;

  }

  loadData(event) {
    setTimeout(() => {
      console.log('Done');
      if (this.tipsList.length >= this.allTLength) {
        event.target.complete();
        this.infiniteScroll.disabled = true;
        return;
      }
      for (let i = 0; i <= Math.floor(this.allTipsList.length / 2); i++) {
        this.tipsList.push(this.allTipsList.pop());
      }

      event.target.complete();
    }, 500);
  }

  sShare(title: string, description: string, image: string) {
    const options = {
      message: title + '\n' + description, // not supported on some apps (Facebook, Instagram),
    };
    this.socialSharing.shareWithOptions(options);
  }

}
