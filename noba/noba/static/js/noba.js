document.addEventListener("DOMContentLoaded", function() {

    // Global
    const isHomePage = document.querySelector('#home-page');
    const isApproachPage =  document.querySelector('.card-approach');
    const header = document.querySelector('header');

    // Menu
    let logoMenu = document.querySelector('.logo-menu');
    let btnMenuClose = document.querySelector('.btn-menu-close');
    let linkMenuNav = document.querySelector('.menu nav');
    let containerMenu = document.querySelector('.container-menu');
    logoMenu.addEventListener("click", (e) => {
        containerMenu.setAttribute('data-visualization', 'true');
    });

    btnMenuClose.addEventListener("click", (e) => {
        containerMenu.setAttribute('data-visualization', 'false');
    });

    linkMenuNav.addEventListener("click", (e) => {
        if(e.target && e.target.tagName == "A"){
            containerMenu.setAttribute('data-visualization', 'false');
        }
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
            // slider.style.cursor = 'grabbing';
        })
    
        slider.addEventListener('mouseup', (e) => {
            sliderGrabbed = false;
            // slider.style.cursor = 'grab';
        })
    
        slider.addEventListener('mouseleave', (e) => {
            sliderGrabbed = false;
        })
    
        slider.addEventListener('mousemove', (e) => {
            if(sliderGrabbed){
                slider.parentElement.scrollLeft -= e.movementX;
            }
        })
    
        // slider.addEventListener('wheel', (e) =>{
        //     e.preventDefault();
        //     console.log('wheel');
        //     console.log('e.deltaY');
        //     console.log(e.deltaY);
        //     console.log('slider.parentElement.scrollLeft');
        //     console.log(slider.parentElement.scrollLeft);
        //     slider.parentElement.scrollLeft += e.deltaY;
        // })

    })

    // function getScrollPercentage(){
    //     return ((slider.parentElement.scrollLeft / (slider.parentElement.scrollWidth - slider.parentElement.clientWidth) ) * 100);
    // }

    // Modal cookie
    const openModalButton = document.querySelectorAll('[data-modal-target]');
    const closeModalButton =  document.querySelectorAll('[data-modal-close]');
    const overlayModal = document.querySelector('.overlay-modal');
    const coockieModal = document.querySelector('.modal-cookie');
    const logoHeader = document.querySelector('.logo');
    const initial = document.querySelector('#initial');
    const spaceInitial = document.querySelectorAll('.sp-initial');
    const fadeText = document.querySelectorAll('.fade-text');

    let coockiesChecked = sessionStorage.getItem("coockies-checked");
    
    if(isHomePage){
        if(coockiesChecked !== "True"){
            // document.body.classList.remove('initial-overflow');
            coockieModal.classList.add('active');
            // overlayModal.classList.add('active');
            header.classList.add('first');
            initial.classList.remove('display-none');
            spaceInitial.forEach( item => {
                item.classList.remove('display-none');
            })

            fadeText.forEach( item => {
                item.classList.remove('appear');
            })
            initial.classList.add('initial');
        } 
    }


    closeModalButton.forEach( button => {
        button.addEventListener("click", () => {
            let modal = button.closest('.modal-cookie');
            closeModal(modal);
        })
    });

    function closeModal(modal){
        if (modal ==  null) return
        modal.classList.remove('active');
        overlayModal.classList.remove('active');
        logoHeader.classList.remove('first-time');
        // header.classList.remove('first');
        header.classList.add('first-clicked');
        initial.classList.add('scale');
        sessionStorage.setItem("coockies-checked", "True");
    }

    // Screen approach
    if(isHomePage || isApproachPage ){
        let containerApproch = document.querySelector('.approach-cards-container');
        containerApproch.addEventListener("click", (e) => {
            let element = e.target.closest('.card-approach-contantainer');
            if(element){
                element.classList.toggle('active');
            }
        });
    }

    // submit form
    const arrowForm = document.querySelector('.arrow-submit-form');
    arrowForm.addEventListener("click", (e) => {
        let form = e.target.closest('form')
        if(form.checkValidity()){
            form.submit();
        } else {
            form.reportValidity()
        }
    });

    // Intersection Observer
    const faders = document.querySelectorAll('.fade-in');
    const options = {
        threshold:1
    };

    const apearsOnScroll = new IntersectionObserver(
        function(entries, apearOnScroll){
            entries.forEach(entry => {
                if(!entry.isIntersecting){
                    return
                } else {
                    entry.target.classList.add('appear');
                    apearsOnScroll.unobserve(entry.target);
                }
            });
        },
        options
    );

    faders.forEach(fader => {
        apearsOnScroll.observe(fader);
    });


    // Intersection Observer Initial
    const faderTexts = document.querySelectorAll('.fade-text');

    const optionsInitial = {
        threshold:0.7,
        rootMargin: '-25% 0% -25% 0%', 
    };

    const apearsOnScrollInitial = new IntersectionObserver(
        function(entries, apearOnScroll){
            entries.forEach(entry => {
                if(!entry.isIntersecting){
                    entry.target.classList.remove('appear');
                } else {
                    entry.target.classList.add('appear');
                    // apearsOnScroll.unobserve(entry.target);
                }
            });
        },
        optionsInitial
    );

    if(coockiesChecked !== "True"){
        faderTexts.forEach(fader => {
            apearsOnScrollInitial.observe(fader);
        });
    }

    // Intersection observer dark sections
    const darkSections = document.querySelectorAll('.dark-sections');

    const optionsDark = {
        threshold: 0,
        rootMargin: '0px 0px -90% 0px', 
    };

    const apearsOnScrollDark = new IntersectionObserver(
        function(entries, apearOnScroll){
            entries.forEach(entry => {
                if(!entry.isIntersecting){
                    header.classList.remove('dark');
                } else {
                    header.classList.add('dark');
                }
            });
        },
        optionsDark
    );

    darkSections.forEach(darkSection => {
        apearsOnScrollDark.observe(darkSection);
    });


});