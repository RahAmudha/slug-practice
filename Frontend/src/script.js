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