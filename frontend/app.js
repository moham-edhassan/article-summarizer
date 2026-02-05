/* frontend/app.js
Author: Mohamed Hassan
This is the JavaScript file for the article summarizer application
*/
//Loading the DOM and running main
document.addEventListener("DOMContentLoaded", pageLoadedMain); 

//Main function: 
function pageLoadedMain(){
    //gets the form element and adds an event listener to it
    const summarizeForm = document.getElementById("summarize-form");
    summarizeForm.addEventListener("submit", summarizeFormSubmitted);
}

//SummarizeFormSubmitted function: 
function summarizeFormSubmitted(event){
    // Prevents the default behavior of the form
    event.preventDefault();
    //Grabs the URL or text from the form
    const url = document.getElementById("url").value.trim();
    const text = document.getElementById("text").value.trim();

    //Validates that either URL or text is provided
    if(!url && !text){
        //Displays an error message if no URL or text is provided
        displayError("Enter a URL or text to summarize");
        //Hides the error message
        hideError();
        //Exits the function if no URL or text is provided
        return;
    }
    //Calls the summarizeArticle function with the URL and text
    summarizeArticle(url, text);
}

//DisplaySummary function: It displays the summary of the article.
function displaySummary(text){
    //Gets the summary element and sets the text content to the summary
    const summaryElement = document.getElementById("summary");
    //replaces the text content of the summary element with the summary
    summaryElement.textContent = text;
}

//DisplayError function: It displays the error message.
function displayError(message){
    //Gets the error-message element 
    const errorElement = document.getElementById("error-message");
    //Sets the text content of the error element to the error message
    errorElement.textContent = message;
    //Removes the hidden class from the error element, showing the error message
    errorElement.classList.remove("hidden");
}

//SetLoadingState function: It sets the loading state of the submit button.
function setLoadingState(isLoading){
    //Gets the submit button 
    const submitButton = document.querySelector("button[type='submit']");
    //If the loading state is true, disable the submit button and change the text to "Summarizing..."
    if(isLoading){
        submitButton.disabled = true;
        submitButton.innerHTML = "Summarizing...";
    }else{
        //If the loading state is false, enable the submit button and change the text to "Summarize"
        submitButton.disabled = false;
        submitButton.innerHTML = "Summarize";
    }
}

//SummarizeArticle function: It sends the request to the server to summarize the article.
function summarizeArticle(url, text){
    //Sets the loading state to true, starting the loading animation
    setLoadingState(true);
    //Creates a new XMLHttpRequest object
    const request = new XMLHttpRequest();
    //Opens a new request to the server to summarize the article
    request.open("POST", "/summarize", true);
    //Sets the content type to JSON
    request.setRequestHeader("Content-Type", "application/json");

    //Adds an event listener to the request to handle the response from the server
    request.addEventListener('load',() =>handleResponse(request));
    //Adds an event listener to the request to handle the error from the server
    request.addEventListener("error",() => handleError("Request has failed. Please try again."));
    //Sends the request to the server to summarize the article
    request.send(JSON.stringify({url, text}));

}

//HandleResponse function: It takes the request and handles the response from the server.
function handleResponse(request){
    //Sets the loading state to false, stops the loading animation
    setLoadingState(false);
    //If the request is successful, parse the response and display the summary
    if(request.status === 200){
        //Parses the response from the server
        const response = JSON.parse(request.responseText);
        //Displays the summary of the article
        displaySummary(response.summary);
        //Hides the error message
        hideError();
    }else{
        //If the request fails, display the error message
        handleError("An error occurred while summarizing the article");
    }
    
}
//HandleError function: 
function handleError(message){
    //Sets the loading state to false, stopping the loading animation
    setLoadingState(false);
    //Displays the error message
    displayError("An error occurred: " + message);

}

//HideError function: I made this function because I needed to errors in muliple places.
function hideError(){
    //Gets the error element and adds the hidden class to it
    const errorElement = document.getElementById("error-message");
    //Adds the hidden class to the error element, hiding it -> to future self
    errorElement.classList.add("hidden");
}