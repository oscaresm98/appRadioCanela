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
  getFecha(fecha:string){
    const date=new Date(fecha);
    return date.getDate() +" "+ this.getMonth(date.getMonth())+" "+date.getFullYear()
  }
  private getMonth(mes:number){
    switch(mes){
      case 0:
        return "Ene.";
      case 1:
        return "Feb.";
      case 2:
        return "Marzo";
      case 3:
        return "Abr.";
      case 4:
        return "Mayo"
      case 5:
        return "Jun."
      case 6:
        return "Jul."
      case 7:
        return "Ag."
      case 8:
        return "Sept."
      case 9:
        return "Oct."
      case 10:
        return "Nov."
      case 11:
        return "Dic."
    }
  }
}
