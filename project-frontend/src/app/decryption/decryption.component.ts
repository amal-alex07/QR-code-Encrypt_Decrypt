import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthserviceService } from '../authservice.service';


@Component({
  selector: 'app-decryption',
  templateUrl: './decryption.component.html',
  styleUrls: ['./decryption.component.css']
})
export class DecryptionComponent implements OnInit {
  image:any
  key:any;
  

  constructor(private auth: AuthserviceService, private router: Router) { }

  ngOnInit(): void {
  }
  decription()
  {
    this.auth. decryption(this.image,this.key).subscribe((res) => {
      console.log(res);
      if (res['message']=='success') {
        console.log(res.token + "this is token");
        this.router.navigate(["/display"], { state: res['secret'] });
      } else {
        alert(res['message']);
      }
    });
  }
  onChange(event:any)
  {
    this.image=event.target.files[0];
    console.log("hai")
  }

}
