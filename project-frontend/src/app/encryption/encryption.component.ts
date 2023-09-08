import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthserviceService } from '../authservice.service';

@Component({
  selector: 'app-encryption',
  templateUrl: './encryption.component.html',
  styleUrls: ['./encryption.component.css']
})
export class EncryptionComponent implements OnInit {
  message:any
  key:any

  constructor(private auth: AuthserviceService, private router: Router) { }

  ngOnInit(): void {
  }

  encription() {
  this.auth. encryption(this.message,this.key).subscribe((res) => {
    console.log(res);
    if (res['message']=='success') {
      console.log(res.token + "this is token");
      this.router.navigate(["/preview"], { state: res['secret'] });
    } else {
      alert(res['message']);
    }
  });
}

}