import { Component, OnInit } from '@angular/core';
import axios from 'axios';

@Component({
  selector: 'app-matches',
  templateUrl: './matches.component.html',
  styleUrls: ['./matches.component.css']
})
export class MatchesComponent implements OnInit {

  public min_age = 16;
  public max_age = 100;
  public animals = false;
  public users = [];

  constructor() { }

  ngOnInit() {
    this.request()
  }


  request () {
    axios.get(`https://jhhd19.infra.labcode.de/api/matches?user_id=2&min_age=${this.min_age}&max_age=${this.max_age}&animals=${this.animals}`).then((res) => {
      this.users = res.data;
    })
  }

}
