import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';
import { Project } from '../models';

@Component({
  selector: 'app-portfolio',
  templateUrl: './portfolio.component.html',
  styleUrls: ['./portfolio.component.css']
})
export class PortfolioComponent implements OnInit {
  portfolioItems: Project[] = [];

  constructor(private dataService: DataService) { }

  ngOnInit(): void {
    this.dataService.getProjects().subscribe((data: Project[]) => {
      this.portfolioItems = data;
    });
  }


}
