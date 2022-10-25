import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { SocialSharing } from '@awesome-cordova-plugins/social-sharing/ngx';
import { DataService } from 'app/services/data/data.service';

@Component({
  selector: 'app-specific-new',
  templateUrl: './specific-new.component.html',
  styleUrls: ['./specific-new.component.scss'],
})
export class SpecificNewComponent implements OnInit {

  constructor(private activatedRoute: ActivatedRoute, private socialSharing: SocialSharing, private data: DataService) { }

  news:any = { }

  allNews:any = []

  lastNews:any = { }
  ngOnInit() {
    let params = this.activatedRoute.snapshot.params;
    let id = parseInt(params["id"])
    
    
    this.data.getNoticiaTip(id).subscribe( e => {
      this.news = e[0]; 
    });
   
    this.data.getNoticias().subscribe( e => {
      this.allNews = e;
      this.lastNews = this.allNews.pop();
    });

  }

  public interactionMaganer(interactions:number){
    let interactionsText;
    if (interactions <= 1000) {
      interactionsText =  interactions.toString()
    }
    if (interactions >= 1000) {
       let temp = Math.round(interactions/1000)
       interactionsText = temp + "k"
    }
    if (interactions >= 1000000) {
      let temp = Math.round(interactions/1000000)
      interactionsText = temp + "mill"
    }

    return interactionsText

  }
  
  sShare(title:string, description:string, image:string){
    var options = {
      message: title + '\n' + description, // not supported on some apps (Facebook, Instagram),
      //files: [image],
    };
    this.socialSharing.shareWithOptions(options);
  }
}
