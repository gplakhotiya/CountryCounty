import { Component, OnInit, Input } from '@angular/core';
import { ApiService } from './api.service';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  title = 'CountryCounty';
  Data = "";
  mainData:any=[];
  constructor(private api: ApiService) {
  }

  getData() {
    if (this.Data != '') {
      this.api.getData().
      subscribe((result)=> {
        for(let i in result )
        this.mainData.append(i);
      })
    }
  }

  sendData(): void {
    if (this.Data != '') {
      this.api.postData(this.Data).subscribe()
    }
    this.getData()
    console.log(this.mainData)
  }
}
