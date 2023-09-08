


import { Component, OnInit } from '@angular/core';
import { AuthserviceService } from '../authservice.service';
import { Router } from '@angular/router';
import { ImageLoaderConfig } from '@angular/common';

@Component({
  selector: 'app-preview',
  templateUrl: './preview.component.html',
  styleUrls: ['./preview.component.css']
})
export class PreviewComponent implements OnInit {
data:any;
img:any;
  
  constructor(private auth: AuthserviceService, private router: Router ) {
    this.data=this.router.getCurrentNavigation()?.extras.state
   
  }
  ngOnInit(): void {
    console.log("hi",this.data);
    this.img="http://localhost:5000/encrypt/download/"+this.data
    console.log(this.img,"amal")
  }

 
  }









