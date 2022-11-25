import { Component, Input, OnInit } from '@angular/core';
import { MenuController } from '@ionic/angular';
import { AuthService } from 'app/services/auth.service';

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.scss'],
})
export class MenuComponent implements OnInit {
  @Input() menuId:string='fisrt';
  @Input() contentId:string='principal';
  paneEnabled:boolean=true;
  username="default";
  constructor(private menuCtrl:MenuController,
    private authService:AuthService) { }

  ngOnInit() {
    const name=this.authService.getUserJson().username
    console.log("USER NAME: ",this.authService.getUserJson())
    if(this.authService.getIsGuest()){
      this.username="Guest";
    }
    else if( name!=null && name!=""){
      this.username=name;
    }
  }
  go(){
    if(this.menuCtrl.isOpen()){
      
    };
  }



}
