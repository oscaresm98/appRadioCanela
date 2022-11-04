import { Component, OnInit } from '@angular/core';
import { DataService } from 'app/services/data/data.service';
import { RadioDataService } from 'app/services/radio/radio.data.service';

@Component({
  selector: 'app-principal',
  templateUrl: './principal.page.html',
  styleUrls: ['./principal.page.scss'],
})
export class PrincipalPage implements OnInit {

  constructor(private radioDataService:RadioDataService,
    private dataService:DataService) { }

  ngOnInit() {
    
  }
}
