import { Component, Input, OnInit } from '@angular/core';
import { LoadingController, AlertController } from '@ionic/angular';
import { RadioService } from 'app/services/radio/radio.service';

import { Station } from 'app/shared/station';

@Component({
  selector: 'app-dial-subpage',
  templateUrl: './dial-subpage.component.html',
  styleUrls: ['./dial-subpage.component.scss'],
})
export class DialSubpageComponent implements OnInit {
  
  @Input() station!: Station;
  @Input() playerIndex!: number;
  isLiking:boolean=false;

  ngOnInit(): void {}
  like(){
    console.log("---LINKIING")
    this.isLiking=!this.isLiking;
  }

}
