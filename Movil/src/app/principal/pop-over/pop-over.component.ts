import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { PopoverController } from '@ionic/angular';

@Component({
  selector: 'app-pop-over',
  templateUrl: './pop-over.component.html',
  styleUrls: ['./pop-over.component.scss'],
})
export class PopOverComponent implements OnInit {

  constructor(private router: Router,private popCtrl:PopoverController) { }

  ngOnInit() {}
  logout(){
    this.router.navigate(['/login']);
    this.popCtrl.dismiss({
      'fromPopUp':"Cerar session"
    })
  }
}
