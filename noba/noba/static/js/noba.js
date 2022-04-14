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

    window.mobileCheck = function() {
        let check = false;
        (function(a){if(/(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows ce|xda|xiino/i.test(a)||/1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(a.substr(0,4))) check = true;})(navigator.userAgent||navigator.vendor||window.opera);
        return check;
      };

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
        slider.style.left = 0;

        slider.addEventListener('mousedown', (e) => {
            sliderGrabbed = true;
            sliderClicked = false;
            console.log('mousedown');
        })
    
        slider.addEventListener('mouseup', (e) => {
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
            if((x - startx) > 0){
                slider.style.left = '0px';
                return;
            }
            let status = (slider.clientWidth - (slider.firstElementChild.clientWidth * 1) - 48 - 10 )* -1;
            if( status > (parseFloat(x) - parseFloat(startx) ) ){
                slider.style.left = status;
                return;
            }
            slider.style.left = `${x - startx}px`; 
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
    let anchorPointGlobal = sessionStorage.getItem("scroll-anchor");
    
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

    if(anchorPointGlobal !== 'False'){
        // console.log('intial scrollAnchor');
        // console.log(anchorPointGlobal);
        let anchorPoint = document.querySelector(anchorPointGlobal);
        if(anchorPoint){
            anchorPoint.scrollIntoView({behavior: "smooth"});
        }
    }

    sessionStorage.setItem("scroll-anchor", "False");
    // scrollAnchor = "False";


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

    // Scroll with anchor url
    let linksAnchor = document.querySelectorAll('[data-anchor]');

    linksAnchor.forEach( (link) => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            let element = e.target.closest('a');
            let hrefValue = element.getAttribute('href');
            let anchorValue = element.dataset.anchor;
            if(anchorValue !== ""){
                sessionStorage.setItem("scroll-anchor", anchorValue);
            }
            if(hrefValue == "" && anchorValue == ""){
                // console.log('element.href');
                // console.log(hrefValue);
                return;
            } 

            if(anchorValue !== ""){
                // console.log('element.anchor');
                // console.log('anchorValue  1');
                // console.log(element.anchor);
                // console.log(element.dataset.anchor);
                sessionStorage.setItem("scroll-anchor", anchorValue);
            }

            if(hrefValue !== ""){
                // console.log('window.location.href');
                window.location.href = hrefValue;
            } else {
                // console.log('anchorValue  2');
                let anchorPoint = document.querySelector(anchorValue);
                anchorPoint.scrollIntoView({behavior: "smooth"});
                sessionStorage.setItem("scroll-anchor", "False");
            }

        });
    });

});

