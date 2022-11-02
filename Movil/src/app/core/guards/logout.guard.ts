import { Injectable } from '@angular/core';
import { CanActivate, Router } from '@angular/router';
import { AuthService } from 'app/services/auth.service';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class LogoutGuard implements CanActivate {
  constructor(private authService:AuthService,
    private router: Router){}
    canActivate(){
      console.log("GUARD LOGOUTT: ",this.authService.getIsAuth(), " ",this.authService.getIsGuest())
    if(!this.authService.getIsAuth() && !this.authService.getIsGuest()){
      return true;
    }
    this.router.navigateByUrl('/principal');
    return false;
  }
}
