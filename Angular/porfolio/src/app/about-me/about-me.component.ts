import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';

@Component({
  selector: 'app-about-me',
  templateUrl: './about-me.component.html',
  styleUrls: ['./about-me.component.css']
})
export class AboutMeComponent implements OnInit {
  aboutMeData: any;

  constructor(private dataService: DataService) { }

  ngOnInit(): void {
    this.dataService.getAboutMe().subscribe(data => {
      this.aboutMeData = data;
    });
  }
}
