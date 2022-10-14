import { Component, OnInit } from '@angular/core';
import { AuthService } from 'app/services/auth.service';
import { DataService } from 'app/services/data/data.service';

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.page.html',
  styleUrls: ['./home-page.page.scss'],
})
export class HomePagePage implements OnInit {

  constructor(private authService: AuthService) { }

  ngOnInit() {
    this.authService.postLogin('tago21','1234');
  }

}
