import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';
import { jsPDF } from 'jspdf';
import html2canvas from 'html2canvas';
import { Title } from '@angular/platform-browser';

@Component({
  selector: 'app-resume',
  templateUrl: './resume.component.html',
  styleUrls: ['./resume.component.css']
})
export class ResumeComponent implements OnInit {
  resumeData: any; // Adjust according to your actual data type

  constructor(private dataService: DataService, private titleService: Title) { }

  ngOnInit() {
    this.titleService.setTitle("My Resume");
    this.dataService.getResume().subscribe(
      data => {
        this.resumeData = data;
        console.log('Resume data:', this.resumeData);
      },
      error => console.error('Error fetching resume data:', error)
    );
  }


  downloadPdf() {
    const resume = document.getElementById('resumeContent');
    if (resume) {
      html2canvas(resume).then(canvas => {
        const imgData = canvas.toDataURL('image/png');
        const doc = new jsPDF({
          orientation: 'portrait',
          unit: 'px',
          format: [canvas.width, canvas.height]
        });
        doc.addImage(imgData, 'PNG', 0, 0, canvas.width, canvas.height);
        doc.save('resume.pdf');
      });
    }
  }
}
