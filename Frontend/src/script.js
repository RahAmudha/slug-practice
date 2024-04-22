// Scripts for index.html

// Get the submit button element
const submitButton = document.querySelector('.submit-btn');

// Add a click event listener to the submit button
submitButton.addEventListener('click', () => {
    // Get the values from the textareas
    const subject_input = document.querySelector('.prompt-subject').value;
    const example_input = document.querySelector('.prompt-example').value;

    // Print the values to the console
    console.log('Prompt 1:', subject_input);
    console.log('Prompt 2:', example_input);
});


// Scripts for practice.html

// Set to cardSlider for easy reference
const cardSlider = document.querySelector('#card-slider');

// Get value of slider
cardSlider.addEventListener('input', () => {
    // Parse the slider's integer value
    const cardCount = parseInt(cardSlider.value);

    // Set to cardDivs for easy reference
    const cardDivs = document.querySelectorAll('.card');

    // Iterate through cards and show/hide number of cards based on slider value
    cardDivs.forEach((card, index) => {
        if (index < cardCount) {
            card.style.display = 'grid';
        } 
        else {
            card.style.display = 'none';
        }
    });
});