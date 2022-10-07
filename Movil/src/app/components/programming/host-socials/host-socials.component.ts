import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-host-socials',
  templateUrl: './host-socials.component.html',
  styleUrls: ['./host-socials.component.scss'],
})
export class HostSocialsComponent implements OnInit {

  @Input() 
  Username: string;
  @Input() 
  url: string;
  /**
   * Numero referente al ID de la red social.
   * 1 - Instagram
   * 2 - Twitter
   * 3 - Facebook
   */
  @Input() 
  social_network: number;


  constructor() { }

  ngOnInit() {}

}
