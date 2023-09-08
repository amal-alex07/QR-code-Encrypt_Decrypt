import { Component, OnInit } from '@angular/core';
import { AuthserviceService } from '../authservice.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-display',
  templateUrl: './display.component.html',
  styleUrls: ['./display.component.css']
})
export class DisplayComponent implements OnInit {
  data:any

  constructor(private auth: AuthserviceService, private router: Router ) {
    this.data=this.router.getCurrentNavigation()?.extras.state
   
  }

  ngOnInit(): void {
    this.data
  }

}
