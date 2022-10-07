/* eslint-disable max-len */
import { Injectable } from '@angular/core';
import { Streaming } from 'app/shared/streaming';

@Injectable({
  providedIn: 'root'
})
export class StreamingService {

  streamings: Streaming[] = [
    {
      platform: 'Facebook',
      url: 'https://www.facebook.com/plugins/video.php?height=314&href=https%3A%2F%2Fwww.facebook.com%2FTeleamazonasEcuador%2Fvideos%2F3351478701738490%2F&show_text=false&width=560&t=0',
      id: 1,
      titulo: 'Titulo 1',
      startHour: '13:00',
      finishHour: '14:00',
      subtitulo: 'Subtitulo 1',
      descripcion: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. At sapiente consequuntur quae alias ea quo, voluptas maiores tempore delectus suscipit, facilis, illum libero dignissimos sunt iste! Qui molestias tenetur quia.',
      img: 'https://www.vidawellnessandbeauty.com/wp-content/uploads/2020/04/panel01-1.jpg'
    },
    {
      platform: 'Youtube',
      url: 'https://www.youtube.com/embed/jfKfPfyJRdk',
      id: 2,
      titulo: 'Titulo 2',
      startHour: '13:00',
      finishHour: '14:00',
      subtitulo: 'Subtitulo 2',
      descripcion: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. At sapiente consequuntur quae alias ea quo, voluptas maiores tempore delectus suscipit, facilis, illum libero dignissimos sunt iste! Qui molestias tenetur quia.',
      img: 'https://www.vidawellnessandbeauty.com/wp-content/uploads/2020/04/panel01-1.jpg'
    },
  ];

  constructor() { }


  getStreamings() {
    return this.streamings;
  }

  getStreamById(id: number) {
    for (const stream of this.streamings) {
      if(stream.id === id){
        return stream;
      }
    }
    return null;
  }
}
