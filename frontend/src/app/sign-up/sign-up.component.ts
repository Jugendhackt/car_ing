import { Component, OnInit } from '@angular/core';
import axios from 'axios';

@Component({
  selector: 'app-sign-up',
  templateUrl: './sign-up.component.html',
  styleUrls: ['./sign-up.component.css']
})
export class SignUpComponent implements OnInit {
  public name;
  public e_mail;
  public age;
  public address;
  public interests;

  constructor() { }

  ngOnInit() {
  }

  register() {
    axios.get(`https://jhhd19.infra.labcode.de/api/registeruser?username=${this.name}&email=${this.e_mail}&age=${this.age}&address=${this.address}&interests=${this.interests}`)
  }

}
