import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { GaugingStationComponent } from './gauging-station/gauging-station.component';
import { PluviometricStationsComponent } from './components/pluviometric-stations/pluviometric-stations.component';
import { ReservoirStationComponent } from './components/reservoir-station/reservoir-station.component';

@NgModule({
  declarations: [
    AppComponent,
    GaugingStationComponent,
    PluviometricStationsComponent,
    ReservoirStationComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
