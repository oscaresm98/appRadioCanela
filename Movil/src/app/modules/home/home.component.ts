import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss'],
})
export class HomeComponent implements OnInit {

  constructor(private _router: Router,
    private _activatedRoute:ActivatedRoute) { }

  ngOnInit() {}
  navigate(path:string){
    this._router.navigateByUrl('/principal/'+path);
    //this._router.navigate([path], {relativeTo: this._activatedRoute});
  }
}
