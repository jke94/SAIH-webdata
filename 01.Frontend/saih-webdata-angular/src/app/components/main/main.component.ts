import { Component, OnInit } from '@angular/core';

export interface Tile {
  color: string;
  cols: number;
  rows: number;
  text: string;
}
@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  tiles: Tile[] = [
    {text: 'Header',  cols: 4, rows: 1, color: 'lightblue'},
    {text: 'Tabs',     cols: 4, rows: 6, color: 'lightblue'},
    {text: 'Footer',  cols: 4, rows: 1, color: '#DDBDF1'}
    
  ];

  constructor() { }

  ngOnInit(): void {
  }

}
