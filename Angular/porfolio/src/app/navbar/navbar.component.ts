import { ChangeDetectorRef, Component } from '@angular/core';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent {
  highContrastMode = false;
  menuActive = false;

  constructor(private cdr: ChangeDetectorRef) { }

  toggleMenu() {
    this.menuActive = !this.menuActive;
    this.cdr.detectChanges(); // Manually trigger change detection
    console.log('Menu Active:', this.menuActive);
  }
}
