import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { ConfigserviceService } from './configservice.service';
import { HttpClient, HttpClientModule } from "@angular/common/http";
import { Router } from '@angular/router';

@Injectable({
    providedIn: 'root'
  })
  export class AuthserviceService {
    
    constructor(private _url:ConfigserviceService, private http: HttpClient, private router: Router) { }
    private _login=this._url.config_url+"login"; 
    private _encrypt=this._url.config_url+"encrypt"; 
     private _upload=this._url.config_url+"decrypt/upload"; 


    loginUser(username:any,password:any){
        let formData: FormData = new FormData(); 
        formData.append('password',password ); 
        formData.append('username',username ); 
        return this.http.post<any>(this._login,formData, {
          withCredentials: true
        })
    
      }

      encryption(message:any,key :any):Observable<any>{
        let formData: FormData = new FormData(); 
        formData.append('message',message); 
        formData.append('key',key ); 

        return this.http.post<any>(this._encrypt,formData, {
          withCredentials: true
        })
      }
  
      decryption(image:any,key :any):Observable<any>{
        let formData: FormData = new FormData(); 
        formData.append('image',image); 
        formData.append('key',key ); 
        

        return this.http.post<any>(this._upload,formData, {
          withCredentials: true
        })
      }

      logout() {
        withCredentials : false;
        this.router.navigate(['']);
      }
  }