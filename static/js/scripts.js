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


let stancewidth = document.getElementById("stancewidth");
let gripwidth = document.getElementById("gripwidth");
let barposition = document.getElementById("barposition");
let bartypeSection = document.getElementById("bartype-section");
let beltSection = document.getElementById("belt-section");
let tempoSection = document.getElementById("tempo-section");
let pauseSection = document.getElementById("pause-section");
let pinSection = document.getElementById("pin-section");
let deadliftstance = document.getElementById("deadliftstance");

let bartype = document.getElementById("bartype");
let belt = document.getElementById("belt");
let tempo = document.getElementById("tempo");
let pause = document.getElementById("pause");
let pin = document.getElementById("pin");

genParamDivs = [bartypeSection, beltSection, tempoSection, pauseSection, pinSection];
genParamInputs = [bartype, belt, tempo, pause, pin];

function disable(exerciseparam){
    exerciseparam.setAttribute('disabled', '');
}

function enable(exerciseparam){
    exerciseparam.removeAttribute('disabled', '');
}

exerciseType.onchange = function() {
    exercise = exerciseType.value;
    console.log(exercise)
    if (exercise == 1){
        console.log(bartype)
        squatform.style.display = "block";
        benchform.style.display = "none";
        deadliftform.style.display = "none";
        let stancewidth = document.getElementById("stancewidth");
        stancewidth.removeAttribute('disabled', '');
        let gripwidth = document.getElementById("gripwidth");
        gripwidth.setAttribute('disabled', '');
        let barposition = document.getElementById("barposition");
        barposition.removeAttribute('disabled', '');
        let deadliftstance = document.getElementById("deadliftstance");
        deadliftstance.setAttribute('disabled', '');
        for (i = 0; i < genParamDivs.length; i++){
            console.log(genParamDivs[i]);
            genParamDivs[i].style.display = "block";
        }
        
        for (i = 0; i < genParamInputs.length; i++){
            console.log(genParamInputs[i]);
            enable(genParamInputs[i]);
        }
        
    } else if (exercise == 2){
        console.log(exercise)
        squatform.style.display = "none";
        benchform.style.display = "block";
        deadliftform.style.display = "none";
        let stancewidth = document.getElementById("stancewidth");
        stancewidth.setAttribute('disabled', '');
        let gripwidth = document.getElementById("gripwidth");
        gripwidth.removeAttribute('disabled', '');
        let barposition = document.getElementById("barposition");
        barposition.setAttribute('disabled', '');
        let deadliftstance = document.getElementById("deadliftstance");
        deadliftstance.setAttribute('disabled', '');
        for (i = 0; i < genParamDivs.length; i++){
            console.log(genParamDivs[i]);
            genParamDivs[i].style.display = "block";
        }
        
        for (i = 0; i < genParamInputs.length; i++){
            console.log(genParamInputs[i]);
            enable(genParamInputs[i]);
        }

    } else if (exercise == 3){
        console.log(exercise)
        squatform.style.display = "none";
        benchform.style.display = "none";
        deadliftform.style.display = "block"
        let stancewidth = document.getElementById("stancewidth");
        stancewidth.setAttribute('disabled', '');
        let gripwidth = document.getElementById("gripwidth");
        gripwidth.setAttribute('disabled', '');
        let barposition = document.getElementById("barposition");
        barposition.setAttribute('disabled', '');
        let deadliftstance = document.getElementById("deadliftstance");
        deadliftstance.removeAttribute('disabled', '');
        for (i = 0; i < genParamDivs.length; i++){
            console.log(genParamDivs[i]);
            genParamDivs[i].style.display = "block";
        }
        
        for (i = 0; i < genParamInputs.length; i++){
            console.log(genParamInputs[i]);
            enable(genParamInputs[i]);
        }

    } else {
        console.log("other exercise")
        squatform.style.display = "none";
        benchform.style.display = "none";
        deadliftform.style.display = "none";
        belt.setAttribute('disabled', '')
        for (i = 0; i < genParamDivs.length; i++){
            console.log(genParamDivs[i]);
            genParamDivs[i].style.display = "none";
        }
        
        for (i = 0; i < genParamInputs.length; i++){
            console.log(genParamInputs[i]);
            disable(genParamInputs[i]);
        }

        let stancewidth = document.getElementById("stancewidth");
        stancewidth.setAttribute('disabled', '');
        let gripwidth = document.getElementById("gripwidth");
        gripwidth.setAttribute('disabled', '');
        let barposition = document.getElementById("barposition");
        barposition.setAttribute('disabled', '');
        let deadliftstance = document.getElementById("deadliftstance");
        deadliftstance.setAttribute('disabled', '');
        }
    }

okayButton = document.getElementById("okay-button");
setInputButton = document.getElementById("set-input-button");
finishedButton = document.getElementById("finished-button");


let setnumber = document.getElementById("setnumber");
setnumber.onchange = function () {
    sets = setnumber.value;
    // enable submit button
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
                "<th>Weight (in KG)</th>"+
                "<th>RPE</th>"+
            "</tr>";
            
    for (i = 1; i <= sets; i++){
        tbl += "<tr>"+
                    "<td><input type='number' required name='reps' class='form-control'></td>"+
                    "<td><input type='number' required name ='weight' class='form-control'></td>"+
                    "<td><input type='number' required name='rpe' class='form-control'></td>"+
                "</tr>";
    }
    tbl += "</table>";

    $("#reps-counter").append(tbl);
}


okayButton.onclick = function() {
    setInputButton.style.display = "block";
    finishedButton.style.display = "block";
}
