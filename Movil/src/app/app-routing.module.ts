import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';


const routes: Routes = [
  {
    path: '',
    redirectTo: 'initial', pathMatch: 'full'
  },
  {
    path: '',
    loadChildren: () => import('./tabs/tabs.module').then(m => m.TabsPageModule)
  },
  {
    path: 'initial',
    loadChildren: () => import('./initial/initial.module').then( m => m.InitialPageModule)
  },
  {
    path: 'login',
    loadChildren: () => import('./login/login.module').then( m => m.LoginPageModule)
  },
  {
    path: 'privacy-policies',
    loadChildren: () => import('./privacy-policies/privacy-policies.module').then( m => m.PrivacyPoliciesPageModule)
  },
  {
    path: 'menu',
    loadChildren: () => import('./menu/menu.module').then( m => m.MenuPageModule)
  },
  {
    path: 'register',
    loadChildren: () => import('./register/register.module').then( m => m.RegisterPageModule)
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
    path: 'live-streaming',
    loadChildren: () => import('./live-streaming/live-streaming.module').then( m => m.LiveStreamingPageModule)
  },
  {
    path: 'streaming-alternative',
    loadChildren: () => import('./streaming-alternative/streaming-alternative.module').then( m => m.StreamingAlternativePageModule)
  },
  {
    path: 'futbol',
    loadChildren: () => import('./futbol-game/futbol-game.module').then( m => m.FutbolGamePageModule)
  },
  {
    path: 'futbol-team',
    loadChildren: () => import('./futbol-team/futbol-team.module').then( m => m.FutbolTeamPageModule)
  },
  {
    path: 'futbol-team/:id',
    loadChildren: () => import('./futbol-team/futbol-team.module').then( m => m.FutbolTeamPageModule)
  },  {
    path: 'home-page',
    loadChildren: () => import('./home-page/home-page.module').then( m => m.HomePagePageModule)
  },
  {
    path: 'slides-noticias',
    loadChildren: () => import('./slides-noticias/slides-noticias.module').then( m => m.SlidesNoticiasPageModule)
  },
  {
    path: 'slides-noticias',
    loadChildren: () => import('./slides-noticias/slides-noticias.module').then( m => m.SlidesNoticiasPageModule)
  },


];


@NgModule({
  imports: [
    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })
  ],
  exports: [RouterModule]
})
export class AppRoutingModule {}
