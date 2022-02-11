document.addEventListener("DOMContentLoaded", function() {

    // Menu
    let logoMenu = document.querySelector('.logo-menu');
    let btnMenuClose = document.querySelector('.btn-menu-close');

    logoMenu.addEventListener("click", (e) => {
        let containerMenu = document.querySelector('.container-menu');
        containerMenu.setAttribute('data-visualization', 'true');
    });

    btnMenuClose.addEventListener("click", (e) => {
        let containerMenu = document.querySelector('.container-menu');
        containerMenu.setAttribute('data-visualization', 'false');
    });

    //Slider
    const sliders = document.querySelectorAll('.slider-inner');
    // const progressBar = document.querySelector('.prog-bar-inner');


    // slider.parentElement.addEventListener('scroll', (e) => {
    //     progressBar.style.width  = `${getScrollPercentage()}%`
    // })
    let sliderGrabbed = false;
    
    sliders.forEach((slider) => {

        slider.addEventListener('mousedown', (e) => {
            sliderGrabbed = true;
            slider.style.cursor = 'grabbing';
        })
    
        slider.addEventListener('mouseup', (e) => {
            sliderGrabbed = false;
            slider.style.cursor = 'grab';
        })
    
        slider.addEventListener('mouseleave', (e) => {
            sliderGrabbed = false;
        })
    
        slider.addEventListener('mousemove', (e) => {
            if(sliderGrabbed){
                slider.parentElement.scrollLeft -= e.movementX;
            }
        })
    
        slider.addEventListener('wheel', (e) =>{
            e.preventDefault();
            console.log('wheel');
            console.log('e.deltaY');
            console.log(e.deltaY);
            console.log('slider.parentElement.scrollLeft');
            console.log(slider.parentElement.scrollLeft);
            slider.parentElement.scrollLeft += e.deltaY;
        })

    })

    // function getScrollPercentage(){
    //     return ((slider.parentElement.scrollLeft / (slider.parentElement.scrollWidth - slider.parentElement.clientWidth) ) * 100);
    // }

    // Modal cookie
    const openModalButton = document.querySelectorAll('[data-modal-target]');
    const closeModalButton =  document.querySelectorAll('[data-modal-close]');
    const overlayModal = document.querySelector('.overlay-modal');
    const logoHeader = document.querySelector('.logo');

    closeModalButton.forEach( button => {
        button.addEventListener("click", () => {
            let modal = button.closest('.modal-cookie')
            closeModal(modal);
        })
    });

    function closeModal(modal){
        if (modal ==  null) return
        modal.classList.remove('active');
        overlayModal.classList.remove('active');
        logoHeader.classList.remove('first-time');
    }


});