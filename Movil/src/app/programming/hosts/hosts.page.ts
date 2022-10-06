import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { DataService } from 'app/services/data/data.service';
import { Host, HostRF } from 'app/shared/host';
import { HostSocial } from 'app/shared/host-social';

@Component({
  selector: 'app-hosts',
  templateUrl: './hosts.page.html',
  styleUrls: ['./hosts.page.scss'],
})
export class HostsPage implements OnInit {

  Socials:Array<HostSocial> = []
  Host:Host;
  Host1:HostRF;
  apiVieja:boolean = true;
  ready:boolean = false;

  constructor(private data:DataService, private activatedRoute:ActivatedRoute) { }

  ngOnInit() {
    let params = this.activatedRoute.snapshot.params;
    let program_id = params["program_id"];
    let host_id = params["host_id"];


    this.data.getLocutoresPrograma(program_id).subscribe(res=>{
      let Locutores = Object.values(res)
      for (let i = 0; i < Locutores.length; i++) {
        if (Locutores[i].id == host_id){
          this.Host1 = Locutores[i] as HostRF
          this.ready = true;
        }
      }
    })

    this.Host = {
      id: 1,
      imagen: 'https://t4.ftcdn.net/jpg/00/64/67/63/360_F_64676383_LdbmhiNM6Ypzb3FM4PPuFP9rHe7ri8Ju.jpg',
      first_name: 'Nombre',
      last_name: 'Apellido',
      emisora: 'Radio Forever'
    }

    this.Socials = [
      {
        host_id:1,
        social_network_id: 1,
        username: "User",
        url:"https://www.instagram.com/"
      },
      {
        host_id:1,
        social_network_id: 2,
        username: "User",
        url:"https://www.twitter.com/"
      },
      {
        host_id:1,
        social_network_id: 3,
        username: "User",
        url:"https://www.facebook.com/"
      },

    ]
  }

}
