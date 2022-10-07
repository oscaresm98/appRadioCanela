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
