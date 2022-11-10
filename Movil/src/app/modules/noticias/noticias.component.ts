import { Component, OnInit, ViewChild } from '@angular/core';
import { SocialSharing } from '@awesome-cordova-plugins/social-sharing/ngx';
import { IonInfiniteScroll } from '@ionic/angular';
import { DataService } from 'app/services/data/data.service';

@Component({
  selector: 'app-noticias',
  templateUrl: './noticias.component.html',
  styleUrls: ['./noticias.component.scss'],
})
export class NoticiasComponent implements OnInit {
  @ViewChild(IonInfiniteScroll, {static: true}) infiniteScroll: IonInfiniteScroll;
  constructor( private socialSharing: SocialSharing, private data: DataService) { }

  allNewsList:any = []
  newsList:any = []
  allNLength; 
    
  ngOnInit() {
    
    this.data.getNoticias().subscribe( e => {
      this.allNewsList = e;
      this.allNLength = this.allNewsList.length;
      for (let i = 0; i < this.allNLength && i < 10; i++) { 
        this.newsList.push(this.allNewsList.pop())
      }
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
  
  loadData(event) {
    setTimeout(() => {
      console.log('Done');
      
      if (this.newsList.length >= this.allNLength) {
        event.target.complete();
        this.infiniteScroll.disabled = true;
        return;
      }
      for (let i = 0; i <= Math.floor(this.allNewsList.length/2); i++) {
        this.newsList.push(this.allNewsList.pop() );
        
      }
      event.target.complete();
    }, 500);
  }
  
  /** TO SET A SEARCHBAR */
  // public data = ['Amsterdam', 'Buenos Aires', 'Cairo', 'Geneva', 'Hong Kong', 'Istanbul', 'London', 'Madrid', 'New York', 'Panama City'];
  // public results = [...this.data];

  // handleChange(event) {

  //   const query = event.target.value.toLowerCase();
  //   this.results = this.data.filter(d => d.toLowerCase().indexOf(query) > -1);
  // }

  sShare(title:string, description:string, image:string){
    var options = {
      message: title + '\n' + description, // not supported on some apps (Facebook, Instagram),
      //files: [image],
    };
    this.socialSharing.shareWithOptions(options);
  }
  
}
