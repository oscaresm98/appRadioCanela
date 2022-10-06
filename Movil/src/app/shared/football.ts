export interface FootballTeam {
    id: number;
    name: string;
    shield: string;
    city: string;
    description: string;
    state: boolean;
}

export interface Tournament {
    id: number;
    name: string;
    place: string;
    state: boolean;
}

export interface MatchFootball {
    idStation: number;
    date: string;
    startHour: string;
    team1: any;
    team2: any;
    scoreTeam1: number;
    scoreTeam2: number;
    event: Tournament;
}
