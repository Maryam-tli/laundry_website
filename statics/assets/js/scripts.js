
// Replace   enter_your_form_action_url_here   with your actual Mailchimp URL
const formActionURL = `enter_your_form_action_url_here`; 


const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]')
const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl))

// Get the value of the dir=""
var textDirectionOfTheDom = document.querySelector('html').getAttribute('dir');



/*  
  -------------------------------------------
  -----      JS for loader-wrapper      -----
  -------------------------------------------
*/

window.addEventListener("load", function(event){
    var loaderWrapper = document.querySelector('.loader-wrapper');
    if (loaderWrapper) {
        loaderWrapper.style.display = "none";
    } 

    // initialize the AOS
    if (typeof AOS === 'object') {
        AOS.init({
            offset: 0,
            once: true,
        });
    }
})



/*  
  ---------------------------------------------------------------------
  -----      JS to update all the current year automatically      -----
  ---------------------------------------------------------------------
*/

var currentYear = new Date().getFullYear();
var currentYearTag = document.getElementsByClassName("current-year");

if (currentYearTag.length > 0) {
    for (var i = 0; i < currentYearTag.length; i++) {
        currentYearTag[i].innerHTML = currentYear;
    }
}





/*  
  -----------------------------------------------
  -----      JS for button back to top      -----
  -----------------------------------------------
*/

let btnBackToTop = document.querySelector(".btn-back-to-top");

function backToTop() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}

// When the user scrolls down 800px from the top of the document, show the button
function scrollbtnBackToTopFun() {
    if ( document.body.scrollTop > 800 || document.documentElement.scrollTop > 800 ) {
        btnBackToTop.style.display = "inline-flex";
    } else {
        btnBackToTop.style.display = "none";
    }
}

window.onscroll = function () {
    if (btnBackToTop) {
        scrollbtnBackToTopFun();
    }
};

// When the user clicks on the button, scroll to the top of the document
if (btnBackToTop) {
    btnBackToTop.addEventListener("click", backToTop);
}



/*  
  --------------------------------------------------
  -----      JS for header top navigation      -----
  --------------------------------------------------
*/

const navigation = document.querySelector('.navigation');
if (navigation) {
    
    navigation.style.transition = 'top 2s';
    let lastScrollTop = 0;

    window.addEventListener('scroll', () => {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

        if (scrollTop > lastScrollTop) {
            // Scrolling down
            if (scrollTop > 300) {
                navigation.classList.add("fixed-top");
                navigation.classList.remove("position-absolute");
                navigation.style.top = '-190px'; // Hide the navigation menu
            }
        } else {
            // Scrolling up
            if (scrollTop > 300) {
                navigation.classList.add("fixed-top");
                navigation.classList.remove("position-absolute");
                navigation.style.top = '0'; // Show the navigation menu
            } else {
                navigation.classList.remove("fixed-top");
                navigation.classList.add("position-absolute");
                navigation.style.top = ''; // Reset top style
            }
        }

        lastScrollTop = scrollTop;
    });
}



/*  
  ----------------------------------------------------------------------------
  -----      JS script associated with subscribers form (Mailchimp)      -----
  ----------------------------------------------------------------------------
*/

(function () {

    // Get all forms with the class "mc-embedded-subscribe-form"
    var mcEmbeddedSubscribeForms = document.querySelectorAll('.mc-embedded-subscribe-form');

    if (mcEmbeddedSubscribeForms.length > 0) {

        mcEmbeddedSubscribeForms.forEach(function (subscribeForm) {

            subscribeForm.setAttribute('action', formActionURL);
            
            subscribeForm.addEventListener('submit', function (e) {
                e.preventDefault();

                // Check for spam
                if(subscribeForm.querySelector('.js-validate-robot').value !== '') { return false }

                // Get url for mailchimp
                var url = this.action.replace('/post?', '/post-json?');
                url = url + "&c=callback";

                // Add form data to object
                var data = '';
                var inputs = this.querySelectorAll('.js-form-inputs input');
                for (var i = 0; i < inputs.length; i++) {
                    data += '&' + inputs[i].name + '=' + encodeURIComponent(inputs[i].value);
                }

                // Create & add post script to the DOM
                var script = document.createElement('script');
                script.src = url + data;
                document.body.appendChild(script);

                // Callback function
                var callback = 'callback';
                window[callback] = function(data) {

                    // Remove post script from the DOM
                    delete window[callback];
                    document.body.removeChild(script);

                    // Display response message
                    var responseDiv = subscribeForm.querySelector('.js-subscribe-response');

                    if (data.msg === "Thank you for subscribing!") {

                        responseDiv.innerHTML = `
                            <div class="alert bg-success bg-opacity-10 d-flex p-3" role="alert">
                                <svg class="bi flex-shrink-0 me-2 text-success-emphasis" fill="currentColor" width="20" height="20" role="img" viewBox="0 0 16 16" aria-label="success:">
                                    <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z"/>
                                </svg>
                                <div class="ps-1">
                                    <h3 class="m-0 fw-semibold text-sm text-success-emphasis">
                                        ${data.msg}
                                    </h3>
                                    <div class="mt-2 text-sm">
                                        <p class="m-0 text-success-emphasis">
                                            Welcome to our newsletter. Get ready for valuable insights delivered directly to your inbox.
                                        </p>
                                    </div>
                                </div>
                            </div>
                        `;

                        subscribeForm.reset();

                    } else if (data.msg === "You're already subscribed, your profile has been updated. Thank you!") {

                        responseDiv.innerHTML = `
                            <div class="alert bg-success bg-opacity-10 d-flex p-3" role="alert">
                                <svg class="bi flex-shrink-0 me-2 text-success-emphasis" fill="currentColor" width="20" height="20" role="img" viewBox="0 0 16 16" aria-label="success:">
                                    <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z"/>
                                </svg>
                                <div class="ps-1">
                                    <h3 class="m-0 fw-semibold text-sm text-success-emphasis">
                                        ${data.msg}
                                    </h3>
                                    <div class="mt-2 text-sm">
                                        <p class="m-0 text-success-emphasis">
                                            Enjoy your subscription: Your profile is ready.
                                        </p>
                                    </div>
                                </div>
                            </div>
                        `;

                        subscribeForm.reset();

                    } else {

                        responseDiv.innerHTML = `
                            <div class="alert bg-warning bg-opacity-10 d-flex p-3" role="alert">
                                <svg class="bi flex-shrink-0 me-2 text-warning-emphasis" fill="currentColor" width="20" height="20" role="img" viewBox="0 0 16 16" aria-label="warning:">
                                    <path d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"/>
                                </svg>
                                <div class="ps-1">
                                    <h3 class="m-0 fw-semibold text-sm text-warning-emphasis">
                                        ${data.msg} 
                                    </h3>
                                    <div class="mt-2 text-sm">
                                        <p class="m-0 text-warning-emphasis">
                                            Oops! It looks like there was an issue processing your subscription. Please try again, We're here to assist!
                                        </p>
                                    </div>
                                </div>
                            </div>
                        `;

                    }

                };
            });
        });
    }

})();



/*  
  ---------------------------------------------------
  -----      JS to embed a video on modal!      -----
  ---------------------------------------------------
*/

var iframeVideo;
var videoSrc;
var videoDataBsTarget;
var videoDataBsTargetModale;
var videoBtn = document.querySelectorAll('.video-btn-modal');

if (videoBtn.length > 0) {
    videoBtn.forEach(element => {
        element.addEventListener('click',function(e){
            videoSrc = element.getAttribute('data-bs-src')
            videoDataBsTarget = element.getAttribute('data-bs-target')

            iframeVideo = document.querySelector(videoDataBsTarget + " .iframeVideo");

            videoDataBsTarget = videoDataBsTarget.slice(1)
            videoDataBsTargetModale = document.getElementById(videoDataBsTarget)

            videoDataBsTargetModale.addEventListener('shown.bs.modal',(e)=>{
                iframeVideo.setAttribute('src', videoSrc + '?autoplay=1&amp;modestbranding=1&amp;showinfo=0')
            })

            videoDataBsTargetModale.addEventListener('hide.bs.modal',(e)=>{
                iframeVideo.setAttribute('src', videoSrc)
            })

        })
    })
}





/*  
  ----------------------------------
  -----      JS for Glide      -----
  ----------------------------------
*/ 



// Select all elements with the class 'glide'
const glideElements = document.querySelectorAll('.glide');

// Loop through each element and create a Glide instance
if (glideElements.length > 0) {
    // Create an object to store the options for each class
    const glideOptions = {
        glideHighLinear: {
            direction: textDirectionOfTheDom,
            type: 'carousel',
            focusAt: 'center',
            startAt: 4,
            perView: 6,
            breakpoints: {
                1400: { perView: 5 },
                1200: { perView: 4 },
                992: { perView: 3 },
                768: { perView: 2 },
                576: { perView: 1 }
            },
            autoplay: true,
            animationDuration: 3000,
            animationTimingFunc: 'linear'
        },

        glideLowGap: {
            direction: textDirectionOfTheDom,
            type: 'carousel',
            perView: 3,
            focusAt: 'center',
            autoplay: 3000,
            gap: 20,
            breakpoints: {
                1400: { perView: 2 },
                1200: { perView: 2 },
                992: { perView: 1 },
                768: { perView: 1 },
                576: { perView: 1 }
            }
        },

        // Add more classes and options as needed
    };

    glideElements.forEach(element => {
        const classList = element.classList;
        const className = classList[1];
        const option = glideOptions[className];

        // Create and mount the Glide instance
        const glide = new Glide(element, option);
        glide.mount();
    });

}



