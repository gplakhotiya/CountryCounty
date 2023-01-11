import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http: HttpClient) {
  }
  API_URL ="http://127.0.0.1:5000/Search";
  getData(){
    return this.http.get(this.API_URL);
  }
  postData(data:string){
    return this.http.post(this.API_URL,data)
    // return this.http.get(this.API_URL,options:{"body":data})
  }
}
