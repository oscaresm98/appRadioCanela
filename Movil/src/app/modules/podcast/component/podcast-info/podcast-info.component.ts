import { Component, Input, OnInit } from '@angular/core';
import { ModalController } from '@ionic/angular';
import { PlayerComponent } from '../player/player.component';

@Component({
  selector: 'app-podcast-info',
  templateUrl: './podcast-info.component.html',
  styleUrls: ['./podcast-info.component.scss'],
})


export class PodcastInfoComponent implements OnInit {
  /**
   * Contiene el objeto Podcast obtenido de la base de datos.
   */
  @Input() 
  podcast: any;

  /**
   * Si es verdadero se muestra la descripcion del podcast
   * en el componente, si es falso esta no se muestra.
   */
  @Input()
  description: boolean;

  message = 'This modal example uses the modalController to present and dismiss modals.';

  date: string;

  months = ['en.', 'febr.', 'mzo.', 'abr.','may.', 'jun.', 'jul.', 'agt.','sept.', 'oct.', 'nov.', 'dic.']
  
  constructor(private modalCtrl:ModalController) { }

  ngOnInit() {
    this.formatDate()
  }

  public formatDate(){
    let tempDate = new Date(this.podcast.fecha)
    this.date = tempDate.getDay() + ' ' + this.months[tempDate.getMonth()]
  }

  async openModal() {
    const modal = await this.modalCtrl.create({
      component: PlayerComponent,
      cssClass: ['modal-player'],
    });
    modal.present();

    const { data, role } = await modal.onWillDismiss();
  }
}
