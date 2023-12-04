import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError, of } from 'rxjs';
import { catchError, map } from 'rxjs/operators';
import { AboutMe, Project, Resume, Skill } from './models';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  private apiUrl = 'http://127.0.0.1:8000';
  private fallbackImages = ['assets/image1.jpg', 'assets/image2.jpg']; // Add paths to your fallback images

  constructor(private http: HttpClient) { }

  private handleError(error: HttpErrorResponse) {
    console.error('Server error:', error);
    if (error.error instanceof ErrorEvent) {
      console.error('Error:', error.error.message);
    } else {
      console.error(`Server returned code ${error.status}, body was: ${error.error}`);
    }
    // Return an observable with a user-facing error message
    return throwError('Something bad happened; please try again later.');
  }

  getAboutMe(): Observable<AboutMe[]> {
    return this.http.get<AboutMe[]>(`${this.apiUrl}/about-me`).pipe(
      catchError(this.handleError)
    );
  }

  getResume(): Observable<Resume[]> {
    return this.http.get<Resume[]>(`${this.apiUrl}/resume`).pipe(
      catchError(this.handleError)
    );
  }

  getSkills(): Observable<Skill[]> {
    return this.http.get<Skill[]>(`${this.apiUrl}/skills`).pipe(
      catchError(this.handleError)
    );
  }

  getProjects(): Observable<Project[]> {
    return this.http.get<Project[]>(`${this.apiUrl}/projects/`).pipe(
      catchError(err => {
        console.error('Error fetching projects:', err);
        return of([]); // Return an empty array if there's an error
      })
    );
  }

  getImages(): Observable<string[]> {
    return this.getProjects().pipe(
      map(projects => {
        if (projects.length === 0) {
          return this.fallbackImages; // Use fallback images if no projects are available
        }
        return projects
          .filter(project => project.image)
          .map(project => project.image);
      })
    );
  }
}
