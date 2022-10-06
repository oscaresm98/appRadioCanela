import { TestBed } from '@angular/core/testing';

import { AuthenticationFirebaseService } from './authentication.service';

describe('AuthenticationService', () => {
  let service: AuthenticationFirebaseService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AuthenticationFirebaseService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
