import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';
import { AboutMe } from '../models';

@Component({
  selector: 'app-about-me',
  templateUrl: './about-me.component.html',
  styleUrls: ['./about-me.component.css']
})
export class AboutMeComponent implements OnInit {
  aboutMeData: AboutMe | null = null; // Changed to a single object
  isLoading: boolean = true; // To handle loading state

  constructor(private dataService: DataService) { }

  ngOnInit(): void {
    this.dataService.getAboutMe().subscribe({
      next: (data: AboutMe[]) => {
        // Assuming the backend returns an array, take the first element
        this.aboutMeData = data[0] || null;
        this.isLoading = false;
      },
      error: (error) => {
        // Handle any errors here
        console.error('Error fetching About Me data', error);
        this.isLoading = false;
      }
    });
  }
}
