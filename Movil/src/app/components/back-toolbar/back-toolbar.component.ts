import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-back-toolbar',
  templateUrl: './back-toolbar.component.html',
  styleUrls: ['./back-toolbar.component.scss'],
})
export class BackToolbarComponent implements OnInit {
  @Input() namePreviousSection:string="";
  constructor() { }

  ngOnInit() {}

}
