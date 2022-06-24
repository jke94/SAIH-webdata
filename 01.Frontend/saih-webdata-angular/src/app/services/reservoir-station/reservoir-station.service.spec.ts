import { TestBed } from '@angular/core/testing';

import { ReservoirStationService } from './reservoir-station.service';

describe('ReservoirStationService', () => {
  let service: ReservoirStationService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ReservoirStationService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
