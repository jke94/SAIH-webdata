import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PluviometricStationsComponent } from './pluviometric-stations.component';

describe('PluviometricStationsComponent', () => {
  let component: PluviometricStationsComponent;
  let fixture: ComponentFixture<PluviometricStationsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PluviometricStationsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PluviometricStationsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
