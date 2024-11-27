import { Component, OnInit } from '@angular/core';
import { DataService } from '../services/data.service';

@Component({
  selector: 'app-names',
  templateUrl: './names.component.html',
  styleUrls: ['./names.component.css']
})
export class NamesComponent implements OnInit {
  names: Array<string> = [];
  groupNumber: number = 0;

  constructor(private dataService: DataService) { }

  ngOnInit() {
    this.getNames();
  }

  getNames(): void {
    this.dataService.getData().subscribe((response => {
      this.groupNumber = response.groupNumber;
      this.names = response.names;
    }))
  }

}
