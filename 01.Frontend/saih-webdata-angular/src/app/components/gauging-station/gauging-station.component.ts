import { Component, OnInit } from '@angular/core';
import { GaugingStationService } from 'src/app/services/gauging-station/gauging-station.service';
import { GaugingStation } from 'src/app/models/gauging-station';


@Component({
  selector: 'app-gauging-station',
  templateUrl: './gauging-station.component.html',
  styleUrls: ['./gauging-station.component.css']
})
export class GaugingStationComponent implements OnInit {

  gaugingStations: GaugingStation[];
  displayedColumns = ['station', 'river', 'lat', 'lng'];

  constructor(private gaugingStationService: GaugingStationService) {
    this.gaugingStations = []
  }

  ngOnInit() {
    this.gaugingStationService.getJSON().subscribe(data => {
      this.gaugingStations = data as GaugingStation[];
      console.log(this.gaugingStations)
    });
  }
}