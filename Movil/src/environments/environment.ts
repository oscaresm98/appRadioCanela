// This file can be replaced during build by using the `fileReplacements` array.
// `ng build --prod` replaces `environment.ts` with `environment.prod.ts`.
// The list of file replacements can be found in `angular.json`.

export const environment = {
  production: false,
  firebase: {
    apiKey: 'AIzaSyCjOmVcoGH2GV8WljPwKcyh2S7SiOrXHds',
    authDomain: 'radioforever-is1-2022.firebaseapp.com',
    projectId: 'radioforever-is1-2022',
    storageBucket: 'radioforever-is1-2022.appspot.com',
    messagingSenderId: '251071856025',
    appId: '1:251071856025:web:581e65934257e5e3df6708'
  },
  REMOTE_BASE_URL: 'https://gruporadios.pythonanywhere.com',
  TOKEN_URL: '/api_generate_token/',
  AUTH_URL:'/api/login/',
  REGISTER_URL:'/api/registro/',
  LOGOUT_URL: '/api/logout/',
  USERDATA_URL: '/api/user/',
  NOTICIA_URL: '/api/noticias/',
  USER_URL: '/api/usuarios/',
};
export const URL = 'https://gruporadios.pythonanywhere.com';
/*
 * For easier debugging in development mode, you can import the following file
 * to ignore zone related error stack frames such as `zone.run`, `zoneDelegate.invokeTask`.
 *
 * This import should be commented out in production mode because it will have a negative impact
 * on performance if an error is thrown.
 */
// import 'zone.js/dist/zone-error';  // Included with Angular CLI.
