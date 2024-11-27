import { Component, OnInit } from '@angular/core';
import { DataService } from '../services/data.service';
import { trigger, state, style, animate, transition, keyframes } from '@angular/animations';
import { interval } from 'rxjs';

@Component({
  selector: 'app-data',
  templateUrl: './data.component.html',
  styleUrls: ['./data.component.css'],
})


export class DataComponent implements OnInit {
  totalWords: number = 0;
  totalTime: number = 0;
  w: number = 0;
  W: number = 0;
  d: number = 0;
  D: number = 0;
  c: number = 0;
  C: number = 0;

  constructor(private dataService: DataService) { }

  ngOnInit() {
    this.getDuration();
    interval(20).subscribe(n => {if(this.w < this.W){this.w++;}})
    interval(8).subscribe(n => {if(this.w >= this.W && this.d < this.D){this.d++;}})
    interval(35).subscribe(n => {if(this.d >= this.D && this.c < this.C){this.c++;}})
  }

  getBackgroundStyle() {return `conic-gradient(#4A5B54 ${this.d}deg, #e2f2e9 0deg 360deg)`;}
  
  getDuration(): void {
    this.dataService.getData().subscribe(response => {
      if (response.totalTime != this.totalTime){
        this.d = 0;
        this.w = 0;
      }
      this.totalTime = response.totalTime;
      this.totalWords = response.wordCount;
      this.C = response.wordCount;
      this.D = this.totalTime/60*360;
      this.W = this.totalWords/160*100;
      if (this.w > 95) {this.w = 95;}
    })
  }

}
