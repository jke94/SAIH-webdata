import { Component, OnInit, ViewChild } from '@angular/core';
import { ReservoirStation } from 'src/app/models/reservoir-station';
import { MatLegacyTableDataSource as MatTableDataSource } from '@angular/material/legacy-table';
import { MatLegacyPaginator as MatPaginator } from '@angular/material/legacy-paginator';
import { MatSort } from '@angular/material/sort';
import { ReservoirStationService } from 'src/app/services/reservoir-station/reservoir-station.service';

@Component({
  selector: 'app-reservoir-station',
  templateUrl: './reservoir-station.component.html',
  styleUrls: ['./reservoir-station.component.css']
})
export class ReservoirStationComponent implements OnInit {

  gaugingStations !: ReservoirStation[];
  dataSource !: MatTableDataSource<ReservoirStation>
  displayedColumns !: string[];

  @ViewChild(MatPaginator, { static: true }) paginator!: MatPaginator;
  @ViewChild(MatSort, { static: true }) sort!: MatSort;

  constructor(private reservoirStationService: ReservoirStationService) {
    this.displayedColumns = ['station', 'river', 'lat', 'lng'];
    this.dataSource = new MatTableDataSource<ReservoirStation>();
  }

  ngOnInit() {
    this.dataSource.paginator = this.paginator;
    this.dataSource.sort = this.sort;

    this.reservoirStationService.getJSON().subscribe(data => {
      this.dataSource.data = data as ReservoirStation[];
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
