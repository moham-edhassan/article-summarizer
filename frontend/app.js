/* frontend/app.js
Author: Mohamed Hassan
This is the JavaScript file for the article summarizer application
*/
document.addEventListener("DOMContentLoaded", pageLoadedMain);

function pageLoadedMain(){
    const summarizeForm = document.getElementById("summarize-form");
    summarizeForm.addEventListener("submit", summarizeFormSubmitted);
}

function summarizeFormSubmitted(event){
    event.preventDefault();
    const url = document.getElementById("url").value.trim();
    const text = document.getElementById("text").value.trim();

    if(!url && !text){
        displayError("Enter a URL or text to summarize");
        return;
    }

    summarizeArticle(url, text);
}

function displaySummary(text){
    const summaryElement = document.getElementById("summary");
    summaryElement.textContent = text;
}

function displayError(message){
    const errorElement = document.getElementById("error-message");
    errorElement.textContent = message;
    errorElement.classList.remove("hidden");
}

function setLoadingState(isLoading){
    const submitButton = document.querySelector("button[type='submit']");
    if(isLoading){
        submitButton.disabled = true;
        submitButton.innerHTML = "Summarizing...";
    }else{
        submitButton.disabled = false;
        submitButton.innerHTML = "Summarize";
    }
}

function summarizeArticle(url, text){
    setLoadingState(true);
    const request = new XMLHttpRequest();
    request.open("POST", "/summarize", true);
    request.setRequestHeader("Content-Type", "application/json");
    request.addEventListener('load',() =>handleResponse(request));
    request.addEventListener("error",() => handleError());
    request.send(JSON.stringify({url, text}));

}

function handleResponse(request){
    setLoadingState(false);
    if(request.status === 200){
        const response = JSON.parse(request,responseText);
        displaySummary(response.summary);
    }else{
        handleError();
    }
    
}

function handleError(){
    setLoadingState(false);
    displayError("An error occurred while summarizing the article");
}