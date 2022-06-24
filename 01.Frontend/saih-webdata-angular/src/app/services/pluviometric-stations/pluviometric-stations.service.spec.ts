import { TestBed } from '@angular/core/testing';

import { PluviometricStationsService } from './pluviometric-stations.service';

describe('PluviometricStationsService', () => {
  let service: PluviometricStationsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(PluviometricStationsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
