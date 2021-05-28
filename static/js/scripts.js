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

let exerciseType = document.getElementById("exercisetype");
let squatform = document.getElementById("squat-section");
let benchform = document.getElementById("bench-section");
let deadliftform = document.getElementById("deadlift-section");

exerciseType.onchange = function() {
    exercise = exerciseType.value;
    console.log(exercise)
    if (exercise == 1){
        console.log(exercise)
        squatform.style.display = "block";
        benchform.style.display = "none";
        deadliftform.style.display = "none";
    } else if (exercise == 2){
        console.log(exercise)
        squatform.style.display = "none";
        benchform.style.display = "block";
        deadliftform.style.display = "none";
    } else if (exercise == 3){
        console.log(exercise)
        squatform.style.display = "none";
        benchform.style.display = "none";
        deadliftform.style.display = "block"
    } else {
        console.log("other exercise")
        squatform.style.display = "none";
        benchform.style.display = "none";
        deadliftform.style.display = "none";
    }
}

let setnumber = document.getElementById("setnumber");
setnumber.onchange = function () {
    sets = setnumber.value;
    console.log(sets)
    $("#reps-counter").empty();

    if (sets > 0){
        createForm(sets);
    }
}

function createForm(sets) {
    var tbl = "";

    tbl = "<table>"+
            "<tr>"+
                "<th>Reps</th>"+
                "<th>Weight</th>"+
                "<th>RPE</th>"+
            "</tr>";
            
    for (i = 1; i <= sets; i++){
        tbl += "<tr>"+
                    "<td><input type='text' name='reps' class='form-control'></td>"+
                    "<td><input type='text' name ='weight' class='form-control'></td>"+
                    "<td><input type='text' name='rpe' class='form-control'></td>"+
                "</tr>";
    }
    tbl += "</table>";

    $("#reps-counter").append(tbl);
}