//  This script is associated with ./assets/php/contact/mailer.php

const alertDangerContact = `
	<div class="alert bg-danger bg-opacity-10 d-flex p-3 mt-4" role="alert">
		<svg class="bi flex-shrink-0 me-2 text-danger-emphasis" fill="currentColor" width="20" height="20" role="img" viewBox="0 0 16 16" aria-label="danger:">
			<path d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"/>
		</svg>
		<div class="ps-1">
			<h3 class="m-0 fw-semibold text-sm text-danger-emphasis">
				Oops! Your message was not sent. 
			</h3>
			<div class="mt-2 text-sm">
				<p class="m-0 text-danger-emphasis">
					Please try again.
				</p>
			</div>
		</div>
	</div>
`;

const alertSuccessContact = `
	<div class="alert bg-success bg-opacity-10 d-flex p-3 mt-4" role="alert">
		<svg class="bi flex-shrink-0 me-2 text-success-emphasis" fill="currentColor" width="20" height="20" role="img" viewBox="0 0 16 16" aria-label="success:">
			<path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z"/>
		</svg>
		<div class="ps-1">
			<h3 class="m-0 fw-semibold text-sm text-success-emphasis">
				Thank you! Your message has been successfully sent. 
			</h3>
			<div class="mt-2 text-sm">
				<p class="m-0 text-success-emphasis">
					We will contact you soon.
				</p>
			</div>
		</div>
	</div>
`;

const alertSecondaryContact = `
	<div class="alert bg-secondary bg-opacity-10 d-flex p-3 mt-4" role="alert">
		<svg class="bi flex-shrink-0 me-2 text-secondary-emphasis" fill="currentColor" width="20" height="20" role="img" viewBox="0 0 16 16" aria-label="secondary:">
			<path d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16zm.93-9.412-1 4.705c-.07.34.029.533.304.533.194 0 .487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703 0-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381 2.29-.287zM8 5.5a1 1 0 1 1 0-2 1 1 0 0 1 0 2z"/>
		</svg>
		<div class="ps-1">
			<h3 class="m-0 fw-semibold text-sm text-secondary-emphasis">
				Thank you for submitting your message. 
			</h3>
			<div class="mt-2 text-sm">
				<p class="m-0 text-secondary-emphasis">
					Please wait a moment while we process it.
				</p>
			</div>
		</div>
	</div>
`;



var myForm = document.getElementById('myForm');

if (myForm !== null) {

myForm.addEventListener('submit', function(event) {


	if (!myForm.checkValidity()) {

        event.preventDefault()
        event.stopPropagation()
	    myForm.classList.add('was-validated')

		// Replace any existing content in the target element and add the new element to it:
		document.getElementById("yourMessageIsSent").innerHTML = '';
		document.getElementById("yourMessageIsSent").innerHTML= alertDangerContact;	
		document.getElementById("sendMessage").disabled = false;

    } else {


	    var data = new FormData(myForm);
	 	document.getElementById("sendMessage").disabled = true;

		// Replace any existing content in the target element and add the new element to it:
		document.getElementById("yourMessageIsSent").innerHTML = '';
		document.getElementById("yourMessageIsSent").innerHTML = alertSecondaryContact;

		// (B) FETCH
		fetch("./assets/php/contact/mailer.php", {
		    method: "post",
		    body: data
		})
		.then((res) => { return res.text(); })
		.then((txt) => {

		  	if (txt === 'Email Sent') {

	 			myForm.reset();

				// Replace any existing content in the target element and add the new element to it:
				document.getElementById("yourMessageIsSent").innerHTML = '';
				document.getElementById("yourMessageIsSent").innerHTML = alertSuccessContact;
 				document.getElementById("sendMessage").disabled = false;

		  	} else {

				// Replace any existing content in the target element and add the new element to it:
				document.getElementById("yourMessageIsSent").innerHTML = '';
				document.getElementById("yourMessageIsSent").innerHTML = alertDangerContact;	
 				document.getElementById("sendMessage").disabled = false;

		  	}
		})
		.catch((err) => { console.log(err); });
		 
		event.preventDefault();
		myForm.classList.remove('was-validated');

	}


}, false)

}