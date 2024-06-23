// Function to show the modal with movie details
function showModal(element) {
    // Find the closest parent element with the class 'banner-slide' or 'movie-thumbnail'
    const parent = element.closest('.banner-slide, .movie-thumbnail');

    // Retrieve the movie details from data attributes
    const title = parent.getAttribute('data-title'); // Get the movie title
    const description = parent.getAttribute('data-description'); // Get the movie description
    const releaseDate = parent.getAttribute('data-release-date'); // Get the release date
    const genre = parent.getAttribute('data-genre'); // Get the genre
    const rating = parent.getAttribute('data-rating'); // Get move rating
    const length = parent.getAttribute('data-length'); // Get the movie length
    const imageCoverUrl = parent.getAttribute('data-image-cover-url'); // Get the URL for the cover image
    const videoUrl = parent.getAttribute('data-video-url'); // Get the URL for the video
    const stars = parent.getAttribute('data-stars'); // Get movie stars data

    // Get the modal element by its ID
    const modal = document.getElementById('movieModal');

    // Update the modal's content with the movie details
    modal.querySelector('.modal-header h2').textContent = title; // Set the title in the modal header
    modal.querySelector('.modal-image').src = imageCoverUrl; // Set the cover image source
    modal.querySelector('.modal-image').alt = `${title} Cover Image`; // Set the alt text for the image
    modal.querySelector('.modal-year').textContent = `Year: ${releaseDate}`; // Set the release year
    modal.querySelector('.modal-genre').textContent = `Genre: ${genre}`; // Set the genre
    modal.querySelector('.modal-rating').textContent = `Rating: ${rating}`; // Set movie rating
    modal.querySelector('.modal-length').textContent = `Length: ${length} min`; // Set the length in minutes
    modal.querySelector('.modal-content p').textContent = description; // Set the description
    modal.querySelector('.modal-stars').textContent = `Starring: ${stars}`;
    modal.querySelector('#watchNowButton').href = videoUrl; // Set the link for the "Watch Now" button to the video URL

    // Store movie ID in a data attribute for later use in adding to the list
    modal.setAttribute('data-movie-id', videoUrl.split('/').pop());

    // Show the modal
    modal.style.display = 'block';
    setTimeout(() => {
        modal.classList.add('modal-show');
    }, 50);
}

// Function to hide the modal
function hideModal() {
    // Get the modal element by its ID
    const modal = document.getElementById('movieModal');

    // Remove the class that shows the modal, which may trigger an animation or transition
    modal.classList.remove('modal-show');

    // Reset button text and state
    const addToListButton = document.getElementById('addToListButton');
    addToListButton.textContent = 'Add to List'; // Reset button text
    addToListButton.disabled = false; // Enable the button

    // Set the display property to 'none' after a short delay to ensure any animations can complete
    setTimeout(() => {
        modal.style.display = 'none';
    }, 300);
}

// Event listener to hide the modal when clicking outside the content
window.onclick = function(event) {
    // Get the modal element by its ID
    const modal = document.getElementById('movieModal');

    // Check if the click event target is the modal element itself (not the content inside it)
    if (event.target === modal) {
        // Call the function to hide the modal
        hideModal();
    }
}
// Function to add the selected movie to the user's list
function addItemToList() {
    const modal = document.getElementById('movieModal');
    var movieID = modal.getAttribute('data-movie-id'); // Get the stored movie ID

    if (!movieID) {
        console.error("Movie ID not found!");
        return;
    }

     // Fetch the CSRF token from a hidden input in your form or meta tag
    var csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

    $.ajax({
        url: "add-to-list/",
        type: "POST",
        data: {
            movie_id: movieID,
            csrfmiddlewaretoken: csrfToken
        },
        success: function(data) {
            $('#addToListButton').text(data.message); // Update the button text with the response message
            $('#addToListButton').prop('disabled', true); // Disable the button to prevent duplicate adds
            console.log("Item added to list!");
        },
        error: function(xhr, errmsg, err) {
            console.error("Error adding item to list: " + errmsg);
        }
    });
}