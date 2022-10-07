/* eslint-disable radix */
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-futbol-team',
  templateUrl: './futbol-team.page.html',
  styleUrls: ['./futbol-team.page.scss'],
})
export class FutbolTeamPage implements OnInit {
  teamId: number;

  constructor(private activatedRoute: ActivatedRoute) { }

  ngOnInit() {
    const params = this.activatedRoute.snapshot.params;
    this.teamId = parseInt(params.id);
  }

}
