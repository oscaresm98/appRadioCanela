import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SlidesService {
  private enterObservable = new BehaviorSubject<boolean>(true);
  private leaveObservable=new BehaviorSubject<boolean>(false);
  constructor() { }
  get EnteringObservable():Observable<boolean>{
    return this.enterObservable.asObservable();
  }
  get LeavingObservable():Observable<boolean>{
    return this.leaveObservable.asObservable();
  }
  set EnteringObservableData(bool:boolean){
    this.leaveObservable.next(bool)
  }
  set LeavingObservableData(bool:boolean){
    this.leaveObservable.next(bool)
  }
}
