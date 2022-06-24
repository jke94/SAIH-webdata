import { Component, OnInit, ViewChild } from '@angular/core';
import { GaugingStation } from 'src/app/models/gauging-station';
import { MatTableDataSource } from '@angular/material/table';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { GaugingStationService } from 'src/app/services/gauging-station/gauging-station.service';


@Component({
  selector: 'app-gauging-station',
  templateUrl: './gauging-station.component.html',
  styleUrls: ['./gauging-station.component.css']
})
export class GaugingStationComponent implements OnInit {

  gaugingStations !: GaugingStation[];
  dataSource !: MatTableDataSource<GaugingStation>
  displayedColumns !: string[];

  @ViewChild(MatPaginator, { static: true }) paginator!: MatPaginator;
  @ViewChild(MatSort, { static: true }) sort!: MatSort;

  constructor(private gaugingStationService: GaugingStationService) {
    this.displayedColumns = ['station', 'river', 'lat', 'lng'];
    this.dataSource = new MatTableDataSource<GaugingStation>();
  }

  ngOnInit() {
    this.dataSource.paginator = this.paginator;
    this.dataSource.sort = this.sort;

    this.gaugingStationService.getJSON().subscribe(data => {
      this.dataSource.data = data as GaugingStation[];
      console.log(this.gaugingStations)
    });
  }

  applyFilter(event: Event) {
    const filterValue = (event.target as HTMLInputElement).value;
    this.dataSource.filter = filterValue.trim().toLowerCase();
    if (this.dataSource.paginator) {
      this.dataSource.paginator.firstPage();
    }
  }
}