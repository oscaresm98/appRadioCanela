import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { SocialSharing } from '@awesome-cordova-plugins/social-sharing/ngx';
import { DataService } from 'app/services/data/data.service';

@Component({
  selector: 'app-specific-tip',
  templateUrl: './specific-tip.page.html',
  styleUrls: ['./specific-tip.page.scss'],
})
export class SpecificTipPage implements OnInit {
  tips: any = {};

  allTips: any = [];

  lastTips: any = {};

  constructor(private activatedRoute: ActivatedRoute, private socialSharing: SocialSharing, private data: DataService) { }


  ngOnInit() {
    const params = this.activatedRoute.snapshot.params;
    const id = parseInt(params["id"]);

    this.data.getNoticiaTip(id).subscribe(e => {
      this.tips = e[0];
    });

    this.data.getTips().subscribe(e => {
      this.allTips = e;
      this.lastTips = this.allTips.pop();
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

  sShare(title: string, description: string, image: string) {
    const options = {
      message: title + '\n' + description, // not supported on some apps (Facebook, Instagram),
      //files: [image],
    };
    this.socialSharing.shareWithOptions(options);
  }

}
