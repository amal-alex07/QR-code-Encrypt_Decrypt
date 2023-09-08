


import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthserviceService } from '../authservice.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  username:any;
  password:any;

  constructor(private auth: AuthserviceService, private router: Router) { }

  ngOnInit(): void {
  }
  loginUser() {
    this.auth.loginUser(this.username,this.password).subscribe((res) => {
      console.log(res);
      if (res['message']=='success') {
        console.log(res.token + "this is token");
       
        this.router.navigate(["/home", ]);
      } else {
        alert(res['message']);
      }
    });
  }

}


// import { Component, OnInit } from '@angular/core';
// // import { ApiService } from '../shared/services/services';

// @Component({
//   selector: 'app-login',
//   templateUrl: './login.component.html',
//   styleUrls: ['./login.component.css']
// })
// export class LoginComponent implements OnInit {
//   loginInfo: any;

//   constructor(
//     // private ApiService: ApiService
//   ) {
    
//    }

//   ngOnInit(): void {
//   }


  
// //   getInfo(){ 
// //     this.ApiService.login().subscribe((res)=>{
// //       console.log(res)
// //        this.loginInfo=res});}
//  }