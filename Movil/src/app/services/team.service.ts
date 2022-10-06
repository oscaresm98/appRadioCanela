import { Injectable } from '@angular/core';
import { FootballTeam } from 'app/shared/football';

@Injectable({
  providedIn: 'root'
})
export class TeamService {

  teams: FootballTeam[] = [
    {
      id:1,
      name: 'Barcelona',
      city: 'Guayaquil',
      description: 'lorem ipsum',
      shield: 'https://www.vidawellnessandbeauty.com/wp-content/uploads/2020/04/panel01-1.jpg',
      state: true
    },
    {
      id:2,
      name: 'Emelec',
      city: 'Guayaquil',
      description: 'lorem ipsum',
      shield: 'https://www.vidawellnessandbeauty.com/wp-content/uploads/2020/04/panel01-1.jpg',
      state: true
    }
  ];

  constructor() { }

  getTeamByID(id: number) {
    for (const team of this.teams) {
      if(team.id === id){
        return team;
      }
    }
    return null;
  }

}
