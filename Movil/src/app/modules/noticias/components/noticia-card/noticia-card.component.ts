import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-noticia-card',
  templateUrl: './noticia-card.component.html',
  styleUrls: ['./noticia-card.component.scss'],
})
export class NoticiaCardComponent implements OnInit {
  @Input() news:any;
  isLiking:boolean=false;

  ngOnInit() {}
  like(){
    this.isLiking=!this.isLiking;
  }
}
