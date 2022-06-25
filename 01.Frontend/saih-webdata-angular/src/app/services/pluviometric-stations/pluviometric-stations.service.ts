import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { PluviometricStation } from 'src/app/models/pluviometric-station';

@Injectable({
  providedIn: 'root'
})
export class PluviometricStationsService {

  constructor(private http: HttpClient) {

    this.getJSON().subscribe(data => {
    });
  }
  public getJSON(): Observable<PluviometricStation[]> {
    return this.http.get<PluviometricStation[]>("./assets/pluviometric-stations.json");
  }
}