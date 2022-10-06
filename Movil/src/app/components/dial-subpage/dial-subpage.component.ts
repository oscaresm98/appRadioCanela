import { Component, Input, OnInit, Directive, HostListener, AfterViewInit, AfterViewChecked, Output} from '@angular/core';
import { IonButton } from '@ionic/angular';
import { Howl } from 'howler';

@Component({
  selector: 'app-dial-subpage',
  templateUrl: './dial-subpage.component.html',
  styleUrls: ['./dial-subpage.component.scss'],
})
export class DialSubpageComponent implements OnInit {

  @Input() nameRadio = '';
  @Input() dial = '';
  @Input() image = '';
  @Input() url = '';

  radioPlayer = null;

  constructor() { }

  ngOnInit() {
    if(!this.radioPlayer){
      this.radioPlayer = new Howl({
        src:[this.url],
        html5: true,
        volume: 1
      });
    }
  }

  activateButton(button: IonButton){
    // eslint-disable-next-line @typescript-eslint/dot-notation
    const icon = button['el'].querySelector('ion-icon');
    if(icon.getAttribute('name') === 'play-outline'){
      icon.setAttribute('name', 'pause-outline');
      this.radioPlayer.play();
    }
    else{
      icon.setAttribute('name', 'play-outline');
      this.radioPlayer.stop();
    }
  }

  cargarDato(){
    console.log('Cargar');
  }

}
