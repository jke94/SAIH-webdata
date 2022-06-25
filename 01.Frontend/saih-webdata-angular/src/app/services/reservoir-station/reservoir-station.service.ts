import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { ReservoirStation } from 'src/app/models/reservoir-station';

@Injectable({
  providedIn: 'root'
})
export class ReservoirStationService {

  constructor(private http: HttpClient) {

    this.getJSON().subscribe(data => {
    });
  }

  public getJSON(): Observable<ReservoirStation[]> {
    return this.http.get<ReservoirStation[]>("./assets/reservoir-station.json");
  }
}
