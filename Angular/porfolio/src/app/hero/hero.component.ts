import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';
import { Title } from '@angular/platform-browser';

@Component({
  selector: 'app-hero',
  templateUrl: './hero.component.html',
  styleUrls: ['./hero.component.css']
})

export class HeroComponent implements OnInit {
  images: string[] = [];
  activeIndex: number = 0;

  constructor(private dataService: DataService, private titleService: Title) { }

  ngOnInit() {
    this.titleService.setTitle("Home Page");
    this.dataService.getImages().subscribe(
      (data) => {
        this.images = data;
      },
      (error) => {
        console.error('Error loading images:', error);
      }
    );
  }

  onCarouselKeydown(event: KeyboardEvent) {
    if (event.key === 'ArrowLeft') {
      this.moveCarousel('prev');
    } else if (event.key === 'ArrowRight') {
      this.moveCarousel('next');
    }
  }

  moveCarousel(direction: string) {
    if (direction === 'prev') {
      this.activeIndex = this.activeIndex > 0 ? this.activeIndex - 1 : this.images.length - 1;
    } else if (direction === 'next') {
      this.activeIndex = this.activeIndex < this.images.length - 1 ? this.activeIndex + 1 : 0;
    }
  }
}
