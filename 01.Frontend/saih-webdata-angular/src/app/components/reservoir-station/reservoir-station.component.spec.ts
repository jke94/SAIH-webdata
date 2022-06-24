import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ReservoirStationComponent } from './reservoir-station.component';

describe('ReservoirStationComponent', () => {
  let component: ReservoirStationComponent;
  let fixture: ComponentFixture<ReservoirStationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ReservoirStationComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ReservoirStationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
