import { Injectable } from '@angular/core';
import { AlertButton, AlertController, LoadingController } from '@ionic/angular';

@Injectable({ providedIn: 'root' })
export class DialogsController {

    constructor(
        private loadingCtrl: LoadingController,
        private alertCtrl: AlertController
    ) {}

    /**
     * Method that create an loading for user feedback
     *
     * @returns The loading modal created
     */
    async createLoadingDialog(loadingMessage: string) {
        const loading = await this.loadingCtrl.create({
            message: loadingMessage, spinner:'circular', mode: 'ios', backdropDismiss: true,
        });
        return loading;
    }


    async createAlertDialog(messageAlert: string, alertButtons: (string|AlertButton)[],
         onCloseFunc: () => any) {
        const alert = await this.alertCtrl.create({
            message: messageAlert, mode: 'ios', buttons: alertButtons
        });
        alert.onDidDismiss().then(() => onCloseFunc());
        return alert;
    }

    /**
     * Method that create an Alert for user feedback
     *
     * @param messageAlert The message that we need to show
     * @param finishFunc A function that executed later press OK button
     * @returns The alert modal created
     */
    async createAlertError(messageAlert: string) {
        const alert = await this.alertCtrl.create({ message: messageAlert, mode: 'ios', buttons: ['OK'] });
        return alert;
    }


}
