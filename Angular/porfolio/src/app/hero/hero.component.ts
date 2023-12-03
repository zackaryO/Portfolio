// hero.component.ts
import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';

@Component({
  selector: 'app-hero',
  templateUrl: './hero.component.html',
  styleUrls: ['./hero.component.css']
})
export class HeroComponent implements OnInit {
  images: string[] = [];

  constructor(private dataService: DataService) { }

  ngOnInit(): void {
    this.dataService.getImages().subscribe((data: string[]) => {
      this.images = data;
    });
  }
}
