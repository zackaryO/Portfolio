import { Component } from '@angular/core';
import { ThemeService } from '../theme.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent {
  highContrastMode = false;

  constructor(private themeService: ThemeService) { }

  toggleHighContrast() {
    this.highContrastMode = !this.highContrastMode;
    this.themeService.toggleHighContrast();
  }

}
