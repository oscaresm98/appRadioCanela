import { Component, Input, OnInit } from '@angular/core';
import { MenuController, PopoverController } from '@ionic/angular';
import { NotificationComponent } from '../notification/notification.component';
import { PopOverComponent } from '../pop-over/pop-over.component';

@Component({
  selector: 'app-toolbar',
  templateUrl: './toolbar.component.html',
  styleUrls: ['./toolbar.component.scss'],
})
export class ToolbarComponent implements OnInit {
  @Input() menuId:string='first';
  constructor(private popCtrl:PopoverController,
    private menuCtrl:MenuController) { }

  ngOnInit() {
    
  }
  async openPopover(e:any){
    const popover=await this.popCtrl.create({
      component: PopOverComponent,
      event:e
    });
    popover.onDidDismiss().then((data:any)=>{
      console.log("Opcion: ",data)
    })
    return await popover.present();
  }
  toggleMenu(){
    //this.menuCtrl.enable(true,this.menuId);
    this.menuCtrl.toggle();
    
  }
  async openNotification(e:any){
    const popover=await this.popCtrl.create({
      component: NotificationComponent,
      event:e
    });
    popover.onDidDismiss().then((data:any)=>{
      console.log("Opcion: ",data)
    })
    return await popover.present();
  }
  

}
