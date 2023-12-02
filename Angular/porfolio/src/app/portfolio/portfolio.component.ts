import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';
import { Project } from '../models';
import { Title } from '@angular/platform-browser';

@Component({
  selector: 'app-portfolio',
  templateUrl: './portfolio.component.html',
  styleUrls: ['./portfolio.component.css']
})
export class PortfolioComponent implements OnInit {
  portfolioItems: Project[] = [];

  constructor(private dataService: DataService, private titleService: Title) { }

  ngOnInit(): void {
    this.titleService.setTitle("Portfolio");
    this.dataService.getProjects().subscribe((data: Project[]) => {
      this.portfolioItems = data;
    });
  }


}
