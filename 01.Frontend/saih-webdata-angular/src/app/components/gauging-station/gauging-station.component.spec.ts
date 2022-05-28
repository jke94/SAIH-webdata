import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GaugingStationComponent } from './gauging-station.component';

describe('GaugingStationComponent', () => {
  let component: GaugingStationComponent;
  let fixture: ComponentFixture<GaugingStationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ GaugingStationComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(GaugingStationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
