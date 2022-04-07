window.onload = function() {
    const body = document.querySelector('body');
    body.classList.remove("preload");
    body.classList.add("postload");
 };

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
    let moved = false;
    let pressed = true;
    let startx = 0;

    sliders.forEach((slider) => {

        slider.addEventListener('mousedown', (e) => {
            sliderGrabbed = true;
            sliderClicked = false;
            console.log('mousedown');

            // slider.style.cursor = 'grabbing';
        })
    
        slider.addEventListener('mouseup', (e) => {
            // console.log('mouseup');
            // console.log('mouseup sliderGrabbed');
            // console.log(sliderGrabbed);
            // console.log('mouseup moved');
            // console.log(moved);
            sliderGrabbed = false;
            if(!moved){
                // console.log('mouseup clicked');
                let card = e.target.closest('.card-highlight');
                if(!card){
                    card = e.target.closest('.card-team-member');
                }
                if(card.dataset.href !== ' '){
                    window.location.href = card.dataset.href;
                }
            }
            moved = false;
            // slider.style.cursor = 'grab';
        })
    
        slider.addEventListener('mouseleave', (e) => {
            sliderGrabbed = false;
            // console.log('mouseleave');
        })
    
        slider.addEventListener('mousemove', (e) => {
            if(sliderGrabbed){
                moved = true;
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

        slider.addEventListener('touchstart', (e) => {
            pressed = true;
            startx = e.targetTouches[0].clientX - slider.offsetLeft;
        }, {passive: true});
        
        slider.addEventListener('touchmove', (e) => {
            if(!pressed) return;
            x = e.targetTouches[0].clientX;
            slider.style.left = `${x - startx}px`;  
            // checkboundary();
        }, {passive: true});

    })

    // function getScrollPercentage(){
    //     return ((slider.parentElement.scrollLeft / (slider.parentElement.scrollWidth - slider.parentElement.clientWidth) ) * 100);
    // }

    //about page
    let containerTeamMember = document.querySelector('.container-team-members');
    if(containerTeamMember){
        containerTeamMember.addEventListener('click',(e) => {
            let card = e.target.closest('.card-team-member');
            if(e.target && card){
                window.location.href = card.dataset.href;
            }
        } );
    }


    // Modal cookie
    const openModalButton = document.querySelectorAll('[data-modal-target]');
    const closeModalButton =  document.querySelectorAll('[data-modal-close]');
    const overlayModal = document.querySelector('.overlay-modal');
    const coockieModal = document.querySelector('.modal-cookie');
    const logoHeader = document.querySelector('.logo');
    const initial = document.querySelector('#initial');
    const spaceInitial = document.querySelectorAll('.sp-initial');
    const fadeText = document.querySelectorAll('.fade-text');
    let firstScroll = false;

    let coockiesChecked = sessionStorage.getItem("coockies-checked");
    let loggedChecked = sessionStorage.getItem("logged-checked");
    
    if(isHomePage){
        if(loggedChecked !== "True"){
            // document.body.classList.remove('initial-overflow');
            // coockieModal.classList.add('active');
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

        if(coockiesChecked !== "True"){
            // removed old modal because there ia newone
            // coockieModal.classList.add('active');
        }
        if (!firstScroll) {

            document.addEventListener('wheel', (e) => {
                if (!firstScroll) {
                    closeInitialAnimation();
                    firstScroll = true;
                }
            });

            document.addEventListener('touchstart', (e) => {
                if (!firstScroll) {
                    closeInitialAnimation();
                    firstScroll = true;
                }        
            });

            document.addEventListener('click', (e) => {
                if (!firstScroll) {
                    closeInitialAnimation();
                    firstScroll = true;
                }        
            });
        }
    }

    // waiting for the modal creation dinamically by iubenda-script
    // https://stackoverflow.com/questions/5525071/how-to-wait-until-an-element-exists
    function waitForElm(selector) {
        return new Promise(resolve => {
            if (document.querySelector(selector)) {
                return resolve(document.querySelector(selector));
            }
    
            const observer = new MutationObserver(mutations => {
                if (document.querySelector(selector)) {
                    resolve(document.querySelector(selector));
                    observer.disconnect();
                }
            });
    
            observer.observe(document.body, {
                childList: true,
                subtree: true
            });
        });
    }

    waitForElm('.iubenda-cs-accept-btn').then((elm) => {
        if(coockiesChecked !== "True"){
            let modalAccepeted = document.querySelector('.iubenda-cs-accept-btn');
            modalAccepeted.addEventListener('click', (e) => {
                sessionStorage.setItem("coockies-checked", "True");
            });        
        } else {
            let modalEuropa = document.querySelector('#iubenda-cs-banner');
            modalEuropa.classList.add('display-none');
        }
    });
    
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
        sessionStorage.setItem("logged-checked", "True");
    }

    function closeInitialAnimation(){
        // if (modal ==  null) return
        // modal.classList.remove('active');
        // overlayModal.classList.remove('active');
        logoHeader.classList.remove('first-time');
        // header.classList.remove('first');
        header.classList.add('first-clicked');
        initial.classList.add('scale');
        sessionStorage.setItem("logged-checked", "True");
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

    // Video
    // It is a helper to allow run the video in safari
    let video = document.getElementById('video-play');
    if(video){
        video.play();
    }

    // submit form
    const validateEmail = (email) => {
        return String(email)
          .toLowerCase()
          .match(
            /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
          );
      };

    const arrowForm = document.querySelector('.arrow-submit-form');
    let errorMessage = document.querySelector('#label-error-message');

    arrowForm.addEventListener("click", (e) => {
        let form = e.target.closest('form')
        let checkbox = form.querySelector('[type="checkbox"]');
        let email = form.querySelector('[type="email"]');
        // debugger;
        if(!checkbox.checked){
            checkbox.setCustomValidity("Invalid field.");
            errorMessage.innerHTML = 'Terms and conditions is not checked';
            errorMessage.classList.remove('display-none');
        } else{
            checkbox.setCustomValidity("");
            // errorMessage.classList.add('display-none');
        }

        if(!validateEmail(email.value)){
            email.setCustomValidity("Invalid field.");
            errorMessage.innerHTML = 'Email field is wrong';
            errorMessage.classList.remove('display-none');
        } else{
            email.setCustomValidity("");
            // errorMessage.classList.add('display-none');
        }
        
        if(form.checkValidity() && checkbox.checked && validateEmail(email.value)){
            form.submit();
        } 
    });

    let checkbox = document.querySelector('#id-agreement');
    checkbox.addEventListener("click", (e) => {
        if(!checkbox.checked){
            checkbox.setCustomValidity("Invalid field.");
        }else{
            checkbox.setCustomValidity("");
            errorMessage.classList.add('display-none');
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

    if(loggedChecked !== "True"){
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

