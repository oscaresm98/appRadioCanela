import { Component, OnInit } from '@angular/core';
import { AuthService } from 'app/services/auth.service';
import { DataService } from 'app/services/data/data.service';

@Component({
  selector: 'app-slides-noticias',
  templateUrl: './slides-noticias.page.html',
  styleUrls: ['./slides-noticias.page.scss'],
})
export class SlidesNoticiasPage implements OnInit {

  constructor(private dataService: DataService) { }

  ngOnInit() {
    this.dataService.getNoticias();
  }

}
