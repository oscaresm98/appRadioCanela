import { Component, Input, OnInit } from '@angular/core';
import { SocialSharing } from '@awesome-cordova-plugins/social-sharing/ngx';

@Component({
  selector: 'app-noticia-card',
  templateUrl: './noticia-card.component.html',
  styleUrls: ['./noticia-card.component.scss'],
})
export class NoticiaCardComponent implements OnInit {
  @Input() news:any;
  isLiking:boolean=false;
  constructor(private socialSharing: SocialSharing,){}
  ngOnInit() {}
  like(){
    this.isLiking=!this.isLiking;
  }
  sShare(title:string, description:string, image:string){
    var options = {
      message: title + '\n' + description, // not supported on some apps (Facebook, Instagram),
      //files: [image],
    };
    this.socialSharing.shareWithOptions(options);
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
  getFecha(fecha:string){
    const date=new Date(fecha);
    return date.getDate() +" "+ this.getMonth(date.getMonth())+" "+date.getFullYear()
  }
  private getMonth(mes:number){
    switch(mes){
      case 1:
        return "Ene.";
      case 2:
        return "Feb.";
      case 3:
        return "Marzo";
      case 4:
        return "Abr.";
      case 5:
        return "Mayo"
      case 6:
        return "Jun."
      case 7:
        return "Jul."
      case 8:
        return "Ag."
      case 9:
        return "Sept."
      case 10:
        return "Oct."
      case 11:
        return "Nov."
      case 12:
        return "Dic."
    }
  }
}
