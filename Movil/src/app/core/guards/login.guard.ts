import { Injectable } from '@angular/core';
import { CanActivate, CanLoad, Route, Router, UrlSegment, UrlTree } from '@angular/router';
import { AuthService } from 'app/services/auth.service';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class LoginGuard implements CanActivate {
  constructor(private authService:AuthService,
    private router: Router){}

    canActivate(){
      console.log("GUARD LOGIN: ",this.authService.getIsAuth(), " ",this.authService.getIsGuest())
    if(this.authService.getIsAuth() || this.authService.getIsGuest()){
      return true;
    }
    this.router.navigateByUrl('/login');
    return false;
  }
}
