/*!
* Start Bootstrap - Landing Page v5.1.0 (https://startbootstrap.com/theme/landing-page)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-landing-page/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

// function to check if passwords are equal

let passwordAlert = document.getElementById("password-alert")

$("#submit-registration").click(function () {
    var password1 = $("#Password1").val();
    var password2 = $("#Password2").val();
    if (password1 != password2){
        passwordAlert.removeAttribute("hidden"); 
        return false;
    }
    return true;
});