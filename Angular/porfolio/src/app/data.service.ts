import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  private apiUrl = 'https://api.com'; // Replace with Django API URL

  constructor(private http: HttpClient) { }

  getAboutMe(): Observable<any> {
    return this.http.get(`${this.apiUrl}/about-me`);
  }

  getPortfolio(): Observable<any> {
    return this.http.get(`${this.apiUrl}/portfolio`);
  }

  getResume(): Observable<any> {
    return this.http.get(`${this.apiUrl}/resume`);
  }

  getSkills(): Observable<any> {
    return this.http.get(`${this.apiUrl}/skills`);
  }
}
