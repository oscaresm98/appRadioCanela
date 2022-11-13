import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';
import { LoginGuard } from './core/guards/login.guard';
import { LogoutGuard } from './core/guards/logout.guard';
import { SplashComponent } from './splash/splash.component';


const routes: Routes = [
  { path: 'splash',
    component: SplashComponent
  },
  {
    path: 'login',
    loadChildren: () => import('./login/login.module').then( m => m.LoginPageModule),
    canActivate:[LogoutGuard]
  },
  {
    path: 'privacy-policies',
    loadChildren: () => import('./privacy-policies/privacy-policies.module').then( m => m.PrivacyPoliciesPageModule)
  },
  {
    path: 'register',
    loadChildren: () => import('./register/register.module').then( m => m.RegisterPageModule),
    canActivate:[LogoutGuard]
  },
  {
    path: 'programming',
    loadChildren: () => import('./programming/programming/programming.module').then( m => m.ProgrammingPageModule)
  },
  {
    path: 'hosts',
    loadChildren: () => import('./programming/hosts/hosts.module').then( m => m.HostsPageModule)
  },
  {
    path: 'profile-edit',
    loadChildren: () => import('./profile-edit/profile-edit.module').then( m => m.ProfileEditPageModule)
  }
  ,
  {
    path: 'register',
    loadChildren: () => import('./register/register.module').then( m => m.RegisterPageModule)
  },
  {
    path: 'programming/:id',
    loadChildren: () => import('./programming/programming/programming.module').then( m => m.ProgrammingPageModule)
  },
  {
    path: 'hosts/:program_id/:host_id',
    loadChildren: () => import('./programming/hosts/hosts.module').then( m => m.HostsPageModule)
  },
  {
    path: 'information',
    loadChildren: () => import('./information/information.module').then( m => m.InformationPageModule)
  },
  {
    path: 'principal',
    loadChildren: () => import('./principal/principal.module').then( m => m.PrincipalPageModule),
    canActivate:[LoginGuard]
  },
  {
    path: 'transmision',
    loadChildren: () => import('./transmision/transmision.module').then( m => m.TransmisionPageModule)
  },
  { path: '**',
    redirectTo:'splash'
  },
];


@NgModule({
  imports: [
    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })
  ],
  exports: [RouterModule]
})
export class AppRoutingModule {}
