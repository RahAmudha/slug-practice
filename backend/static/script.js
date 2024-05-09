$(document).ready(function() {
    let currentCardIndex = 0;
    let flipCards = [];

    function createFlipCard(question, answer) {
        return `
            <div class="flip-card">
                <div class="flip-card-front">${question}</div>
                <div class="flip-card-back">${answer}</div>
            </div>
        `;
    }

    function displayFlipCards() {
        $('#flip-cards-container').empty();
        if (flipCards.length > 0) {
            $('#flip-cards-container').append(flipCards[currentCardIndex]);
        }
    }

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

        $.ajax({
            url: 'http://127.0.0.1:5000/openai/generate', 
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(data),
            success: function(response) {
                flipCards = response.map(item => createFlipCard(item.question, item.answer));
                currentCardIndex = 0;
                displayFlipCards();
            },
            error: function(xhr, status, error) {
                console.error('Error:', error);
            }
        });
    });

    $('#generate1').click(function() {
        const subject = $('#subject').val().trim();
        const prompt = $('#prompt').val().trim();
        const difficulty = $('#difficulty').val().trim();
        const format = $('#format').val().trim();

        if (!subject || !prompt || !difficulty || !format) {
            alert('Please enter all the fields - subject, example and difficulty.');
            return;
        }

        // Replace this with the actual API call
        cardsData = [
            {
            "question": "What is a semaphore in computer science?",
            "answer": "A semaphore is a synchronization primitive that controls access to a shared resource by multiple processes or threads."
            },
            {
            "question": "What is the difference between process and thread?",
            "answer": "A process is an independent program execution unit, while a thread is a subset of a process that can be scheduled independently for execution."
            }
        ];

        displayCard(currentCardIndex);
        hidePrompts();
    });

    $('#prev').click(function() {
        if (currentCardIndex > 0) {
            currentCardIndex--;
            alert(currentCardIndex);
            displayCard(currentCardIndex);
        }
    });

    $('#next').click(function() {
        if (currentCardIndex < cardsData.length - 1) {
            currentCardIndex++;
            alert(currentCardIndex);
            displayCard(currentCardIndex);
        }
    });

    function displayCard(index) {
        const card = cardsData[index];
        // TODO: fix buttons not working
        console.log(card.question + '\n' + card.answer);
        const flipCardHtml = `
        <button id="prev"><</button>
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <h2>QUESTION</h2>
                    <p>${card.question}</p>
                </div>
                <div class="flip-card-back">
                    <h2>ANSWER</h2>
                    <p>${card.answer}</p>
                </div>
            </div>
        </div>
        <button id="next">></button>
        `;
    
        $('#flip-cards-container').html(flipCardHtml).show();
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