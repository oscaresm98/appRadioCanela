import { TestBed } from '@angular/core/testing';

import { StopRadioService } from './stop-radio.service';

describe('StopRadioService', () => {
  let service: StopRadioService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(StopRadioService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
