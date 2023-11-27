import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';

@Component({
  selector: 'app-portfolio',
  templateUrl: './portfolio.component.html',
  styleUrls: ['./portfolio.component.css']
})
export class PortfolioComponent implements OnInit {
  portfolioItems: any[] = [];

  constructor(private dataService: DataService) { }

  ngOnInit(): void {
    this.getPortfolioItems();
  }

  getPortfolioItems(): void {
    this.dataService.getPortfolio().subscribe(
      (data) => {
        this.portfolioItems = data;
      },
      (error) => {
        console.error('Error fetching portfolio data:', error);
        // Handle error here
      }
    );
  }
}
