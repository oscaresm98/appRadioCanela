import { Injectable } from '@angular/core';
import { MatchFootball } from 'app/shared/football';

@Injectable({
  providedIn: 'root'
})
export class FootballService {

  matches: MatchFootball[] = [
    {
      idStation: 1,
      date: '16/9/2022',
      startHour: '16:00',
      scoreTeam1: 0,
      scoreTeam2: 0,
      team1: {
        id: 1,
        name: 'Barcelona',
        shield: 'https://www.vidawellnessandbeauty.com/wp-content/uploads/2020/04/panel01-1.jpg'
      },
      team2: {
        id: 2,
        name: 'Emelec',
        shield: 'https://www.vidawellnessandbeauty.com/wp-content/uploads/2020/04/panel01-1.jpg'
      },
      event: {
        id: 1,
        name: 'Campeonato Ecuador',
        place: 'Ecuador',
        state: true
      }
    },
    {
      idStation: 2,
      date: '15/9/2022',
      startHour: '16:00',
      scoreTeam1: 3,
      scoreTeam2: 2,
      team1: {
        name: 'Barcelona',
        shield: 'https://www.vidawellnessandbeauty.com/wp-content/uploads/2020/04/panel01-1.jpg'
      },
      team2: {
        name: 'Emelec',
        shield: 'https://www.vidawellnessandbeauty.com/wp-content/uploads/2020/04/panel01-1.jpg'
      },
      event: {
        id: 1,
        name: 'Campeonato Ecuador',
        place: 'Ecuador',
        state: true
      }
    },
    {
      idStation: 3,
      date: '16/9/2022',
      startHour: '16:00',
      scoreTeam1: 0,
      scoreTeam2: 0,
      team1: {
        id: 1,
        name: 'Barcelona',
        shield: 'https://www.vidawellnessandbeauty.com/wp-content/uploads/2020/04/panel01-1.jpg'
      },
      team2: {
        id: 2,
        name: 'Emelec',
        shield: 'https://www.vidawellnessandbeauty.com/wp-content/uploads/2020/04/panel01-1.jpg'
      },
      event: {
        id: 1,
        name: 'Campeonato Ecuador',
        place: 'Ecuador',
        state: true
      }
    },
    {
      idStation: 4,
      date: '15/9/2022',
      startHour: '16:00',
      scoreTeam1: 3,
      scoreTeam2: 2,
      team1: {
        name: 'Barcelona',
        shield: 'https://www.vidawellnessandbeauty.com/wp-content/uploads/2020/04/panel01-1.jpg'
      },
      team2: {
        name: 'Emelec',
        shield: 'https://www.vidawellnessandbeauty.com/wp-content/uploads/2020/04/panel01-1.jpg'
      },
      event: {
        id: 1,
        name: 'Campeonato Ecuador',
        place: 'Ecuador',
        state: true
      }
    },
    {
      idStation: 5,
      date: '16/9/2022',
      startHour: '16:00',
      scoreTeam1: 0,
      scoreTeam2: 0,
      team1: {
        id: 1,
        name: 'Barcelona',
        shield: 'https://www.vidawellnessandbeauty.com/wp-content/uploads/2020/04/panel01-1.jpg'
      },
      team2: {
        id: 2,
        name: 'Emelec',
        shield: 'https://www.vidawellnessandbeauty.com/wp-content/uploads/2020/04/panel01-1.jpg'
      },
      event: {
        id: 1,
        name: 'Campeonato Ecuador',
        place: 'Ecuador',
        state: true
      }
    },
    {
      idStation: 6,
      date: '15/9/2022',
      startHour: '16:00',
      scoreTeam1: 3,
      scoreTeam2: 2,
      team1: {
        name: 'Barcelona',
        shield: 'https://www.vidawellnessandbeauty.com/wp-content/uploads/2020/04/panel01-1.jpg'
      },
      team2: {
        name: 'Emelec',
        shield: 'https://www.vidawellnessandbeauty.com/wp-content/uploads/2020/04/panel01-1.jpg'
      },
      event: {
        id: 1,
        name: 'Campeonato Ecuador',
        place: 'Ecuador',
        state: true
      }
    },
  ];

  constructor() { }

  getAllMatches() {
    return this.matches;
  }

}
