import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { FootballService } from 'app/services/football.service';
import { FootballTeam } from 'app/shared/football';

@Component({
  selector: 'app-equipo',
  templateUrl: './equipo.component.html',
  styleUrls: ['./equipo.component.scss'],
})
export class EquipoComponent implements OnInit {
  team: FootballTeam = {
    id: -1, ciudad: '', descripcion:'', equipo:'', imagen:'', estado: false, redes_sociales: null
  };

  constructor(
    private activatedRoute: ActivatedRoute,
    private footballService: FootballService
  ) { }

  ngOnInit() {
    const params = this.activatedRoute.snapshot.params;
    const idTeam = parseInt(params.id);
    this.footballService.getTeamInfo(idTeam).subscribe(resp => {
      this.team = resp as FootballTeam;
    });
  }

}
