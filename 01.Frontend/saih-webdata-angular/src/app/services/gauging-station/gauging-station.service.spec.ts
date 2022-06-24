import { TestBed } from '@angular/core/testing';

import { GaugingStationService } from './gauging-station.service';

describe('GaugingStationService', () => {
  let service: GaugingStationService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(GaugingStationService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
