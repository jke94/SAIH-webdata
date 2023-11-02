import { Component, OnInit, ViewChild } from '@angular/core';
import { PluviometricStation } from 'src/app/models/pluviometric-station';
import { MatLegacyTableDataSource as MatTableDataSource } from '@angular/material/legacy-table';
import { MatLegacyPaginator as MatPaginator } from '@angular/material/legacy-paginator';
import { MatSort } from '@angular/material/sort';
import { PluviometricStationsService } from 'src/app/services/pluviometric-stations/pluviometric-stations.service';

@Component({
  selector: 'app-pluviometric-stations',
  templateUrl: './pluviometric-stations.component.html',
  styleUrls: ['./pluviometric-stations.component.css']
})
export class PluviometricStationsComponent implements OnInit {

  gaugingStations !: PluviometricStation[];
  dataSource !: MatTableDataSource<PluviometricStation>
  displayedColumns !: string[];

  @ViewChild(MatPaginator, { static: true }) paginator!: MatPaginator;
  @ViewChild(MatSort, { static: true }) sort!: MatSort;

  constructor(private pluviometricStationsService: PluviometricStationsService) {
    this.displayedColumns = ['station', 'river', 'lat', 'lng'];
    this.dataSource = new MatTableDataSource<PluviometricStation>();
  }

  ngOnInit() {
    this.dataSource.paginator = this.paginator;
    this.dataSource.sort = this.sort;

    this.pluviometricStationsService.getJSON().subscribe(data => {
      this.dataSource.data = data as PluviometricStation[];
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
