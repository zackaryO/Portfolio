import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ThemeService {
  private highContrastEnabled = new BehaviorSubject<boolean>(false);

  toggleHighContrast() {
    this.highContrastEnabled.next(!this.highContrastEnabled.value);
  }

  isHighContrastEnabled() {
    return this.highContrastEnabled.asObservable();
  }
}
