$(document).ready(function() {
    let currentCardIndex = 0;
    let cardsData = [];
  
    $('#generate').click(function() {
        const subject = $('#subject').val().trim();
        const prompt = $('#prompt').val().trim();
        const difficulty = $('#difficulty').val().trim();
        const format = $('#format').val().trim();
  
        if (!subject || !prompt || !difficulty || !format) {
            alert('Please enter all the fields - subject, example and difficulty.');
            return;
        }
  
        const data = {
            "topic": subject,
            "example": prompt,
            "difficulty": difficulty,
            "format": format
        };

        // Show the loading symbol
        $('#loadingSymbol').show();

        var $button = $(this); // Cache the button element
        $button.prop('disabled', true); // Disable the button
  
        $.ajax({
            url: 'http://127.0.0.1:5000/openai/generate', 
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(data),
            success: function(response) {
                if (response.status === 'bueno') {
                    cardsData = response.questions;
                    hideLogo();
                    displayCard(currentCardIndex);
                    displayButtons();
                    hidePrompts();
                  } else {
                    alert('Error fetching data');
                  }
            },
            error: function(xhr, status, error) {
                // alert('Error fetching data');
                console.error('Error:', error);
            },
            complete: function() {
                // alert('Data fetched successfully');
                // $('#generate').html('Generate').prop('disabled', false);
                $('#loadingSymbol').hide();
                $button.prop('disabled', false);
            }
  
        });
    });
  
    function displayButtons() {
        const navButtons = `
        <button id="prev" class="nav-button">&lt;</button>
        <button id="next" class="nav-button">&gt;</button><br>
        `;
    
        $('#buttons').html(navButtons).show();
    }
  
    // Event delegation for dynamically added buttons
    $('.container').on('click', '.nav-button', function() {
        const buttonId = $(this).attr('id');
        if (buttonId === 'prev' && currentCardIndex > 0) {
        currentCardIndex--;
        } else if (buttonId === 'next' && currentCardIndex < cardsData.length - 1) {
        currentCardIndex++;
        }
        displayCard(currentCardIndex);
    });

    // When the user clicks on the help link, open the modal
    $('#homeLink').on('click', function() {
        // alert("Home link clicked");

        if ($('#flip-cards-container').is(':visible')) {
            // hide the flip cards container
            $('#flip-cards-container').hide();
            $('#buttons').hide();
            
            // reset & show the logo and prompt entry fields
            $('#logo').show();

            $('#subject').show();
            $('#subject').val('');

            $('#prompt').show();
            $('#prompt').val('');

            $('#difficulty').show();
            $('#difficulty').trigger('reset');

            $('#format').show();
            $('#format').trigger('reset');

            $('#generate').show();
        }
    });

    $('#generate').on('click', function() { 
        var $button = $(this); // Cache the button element
        $button.prop('disabled', true); // Disable the button
    }); 

    // When the user clicks on the help link, open the modal
    $('#helpLink').on('click', function() {
        $('#myModal').show();
    });

    // When the user clicks on <span> (x), close the modal
    $('.close').on('click', function() {
        $('#myModal').hide();
    });

    // When the user clicks anywhere outside of the modal, close it
    $(window).on('click', function(event) {
        if ($(event.target).is('#myModal')) {
        $('#myModal').hide();
        }
    });
    
    function displayCard(index) {
        const card = cardsData[index];
        console.log(card.question + '\n' + card.answer);

        const format = document.getElementById('format').value;
        
        // If multiple choice format, show choices
        // TODO: have to check if JSON is "choices" or "choice"
        if (format === 'mc' && (card.choices || card.choice)) {
            card.choices_list = '<ul>';
            if (card.choices) {
                for (let choice of card.choices) {
                    card.choices_list += `<li>${choice}</li>`;
                }
                card.choices_list += '</ul>';
            }
            else if (card.choice) {
                for (let choice of card.choice) {
                    card.choices_list += `<li>${choice}</li>`;
                }
                card.choices_list += '</ul>';
            }
        }
        
        // If this wasn't multiple choice, this would yield undefined/null
        // console.log(card.choices_list);

        // If the card.choices_list string is existent, print to front of card
        // otherwise, do not show anything
        const flipCardHtml = `
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <h2>QUESTION</h2>
                    <p>${card.question}</p>
                    ${card.choices_list ? `<p>${card.choices_list}</p>` : ''}
                </div>
                <div class="flip-card-back">
                    <h2>ANSWER</h2>
                    <p>${card.answer}</p>
                </div>
            </div>
        </div>
        `;
    
        $('#flip-cards-container').html(flipCardHtml).show();
    }
  
    function hideLogo() {
        $('#logo').hide();
    }

    function hidePrompts() {
        $('#subject').hide();
        $('#prompt').hide();
        $('#difficulty').hide();
        $('#format').hide();
        $('#generate').hide();
        $('#generate1').hide();
    }
  });
  
