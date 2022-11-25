import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { SlidesService } from '../services/slides.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss'],
})
export class HomeComponent implements OnInit {
  entering:boolean=true;
  leaving:boolean=false;
  autoplay=true;
  constructor(private _router: Router,
    private _activatedRoute:ActivatedRoute,
    private slidesService:SlidesService) { }

  ngOnInit() {}
  navigate(path:string){
    this._router.navigateByUrl('/principal/'+path);
    //this._router.navigate([path], {relativeTo: this._activatedRoute});
  }
  ionViewWillLeave(){
    console.log("LEAVING METHOD")
    this.autoplay=false;
    }
    ionViewWillEnter() {
      console.log("ENTERRR METHOD")
      this.autoplay=true;
    }
  
}
