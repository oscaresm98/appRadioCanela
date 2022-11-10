import { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'io.ionic.radioRedonda',
  appName: 'Radio Redonda',
  webDir: 'www',
  bundledWebRuntime: false,
  plugins: {
    LocalNotifications: {
      smallIcon: 'ic_stat_icon_config_sample',
      iconColor: '#488AFF',
    },
    FirebaseAuthentication: {
      skipNativeAuth: false,
      providers: ['google.com', 'facebook.com', 'apple.com']
    }
  }
};

export default config;
