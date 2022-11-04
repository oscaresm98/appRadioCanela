import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { FootballGame } from 'app/shared/football';
import { environment } from 'environments/environment.prod';
import { Observable } from 'rxjs';
import { map, take } from 'rxjs/operators';
import { URL } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class FootballService {
  private gamesPlayedURL = `${URL}/api/partidos_jugados`;
  private gamesToPlayURL = `${URL}/api/partidos_por_jugar`;

  private teamURL = `${URL}/api/equipos/`;

  constructor(private http: HttpClient) { }

  getAllMatches() {
    // return this.matches;
  }


  getAllGamesPlayed(): Observable<FootballGame[]> {
    return this.http.get<FootballGame[]>(this.gamesPlayedURL).pipe( take(1) );
  }

  getAllGamesToPlay() {
    return this.http.get<FootballGame[]>(this.gamesToPlayURL).pipe( take(1) );
  }

  getTeamInfo(idTeam: number) {
    const urlTeam = this.teamURL + idTeam.toString();
    return this.http.get(urlTeam);
  }

}
