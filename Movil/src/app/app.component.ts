import { Component, OnInit } from '@angular/core';
import { Storage } from '@ionic/storage-angular';
import { DataService } from './services/data/data.service';
import { RadioDataService } from './services/radio/radio.data.service';

@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.scss'],
})
export class AppComponent implements OnInit{
  constructor(private storage: Storage,
    private dataService: DataService,
    private radioDataService: RadioDataService) {}
  async ngOnInit(): Promise<void> {
    await this.storage.create();
    await this.obtenerRadio();
    
    await this.getPublicidad();
  }
  
  private getPublicidad(){
    this.dataService.obtenerPublicidad();
  }
  private async obtenerRadio(){
    await this.radioDataService.obtenerRadioRedondaRequest().then(
      (data:any)=>{
        if (data.resCode == 0) {
          console.log("Radios: ",this.radioDataService.getRadioRedondaData())
        } else {
          console.log("ERROR AL OBTEBER NOCTICIAS")
        }
      }
      );
  }
}
