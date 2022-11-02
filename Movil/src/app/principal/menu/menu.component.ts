import { Component, Input, OnInit } from '@angular/core';
import { MenuController } from '@ionic/angular';

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.scss'],
})
export class MenuComponent implements OnInit {
  @Input() menuId:string='fisrt';
  @Input() contentId:string='principal';
  paneEnabled:boolean=true;
  constructor(private menuCtrl:MenuController) { }

  ngOnInit() {
  }
  go(){
    if(this.menuCtrl.isOpen()){
      
    };
  }



}
