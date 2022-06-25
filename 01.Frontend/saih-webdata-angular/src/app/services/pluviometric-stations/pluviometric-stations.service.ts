import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { GaugingStation } from 'src/app/models/gauging-station';

@Injectable({
  providedIn: 'root'
})
export class PluviometricStationsService {

  constructor(private http: HttpClient) {

    this.getJSON().subscribe(data => {
    });
  }
  public getJSON(): Observable<GaugingStation[]> {
    return this.http.get<GaugingStation[]>("./assets/pluviometric-stations.json");
  }
}