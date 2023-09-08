import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ConfigserviceService {

  public config_url="http://localhost:5000/"

  constructor() { }
}
