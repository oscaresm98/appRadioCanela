/* eslint-disable max-len */
/* eslint-disable no-underscore-dangle */
/* eslint-disable prefer-arrow/prefer-arrow-functions */
export const moveSegment = (element: any, idSegment: string): void => {
    const s= element.getBoundingClientRect();
    const sw=(s.right-s.left);

    for (const button of element.childNodes) {
        if(button.id === idSegment){
            const bc = button.offsetLeft+(button.offsetWidth/2);
            const diff = bc-(sw/2);
            element.scrollTo({
                left: diff,
                behavior: 'smooth'
            });
        }
    }
};

export const getUrlFacebookVideo = (url: string) => `https://www.facebook.com/v2.3/plugins/video.php?autoplay=true&container_width=800&href=${url}&locale=en_US&sdk=joey`;


/**
 * Utils for dates
 */

export const isLaterDate = (dateString: string) => {
    const today = new Date();
    today.setHours(0,0,0,0);
    return new Date(dateString).getTime() >= today.getTime();
};
