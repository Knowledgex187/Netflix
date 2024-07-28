// Function to show the modal with movie details
function showModal(element) {
    // Find the closest parent element with the class 'banner-slide' or 'movie-thumbnail'
    const parent = element.closest('.banner-slide, .movie-thumbnail');

    // Retrieve the movie details from data attributes of the parent element
    const title = parent.getAttribute('data-title'); // Get the movie title
    const description = parent.getAttribute('data-description'); // Get the movie description
    const releaseDate = parent.getAttribute('data-release-date'); // Get the movie release date
    const genre = parent.getAttribute('data-genre'); // Get the movie genre
    const rating = parent.getAttribute('data-rating'); // Get the movie rating
    const length = parent.getAttribute('data-length'); // Get the movie length in minutes
    const imageCoverUrl = parent.getAttribute('data-image-cover-url'); // Get the URL for the cover image
    const videoUrl = parent.getAttribute('data-video-url'); // Get the URL for the video
    const stars = parent.getAttribute('data-stars'); // Get the movie stars

    // Get the modal element by its ID
    const modal = document.getElementById('movieModal');

    // Update the modal's content with the retrieved movie details
    modal.querySelector('.modal-header h2').textContent = title; // Set the movie title
    modal.querySelector('.modal-image').src = imageCoverUrl; // Set the cover image source
    modal.querySelector('.modal-image').alt = `${title} Cover Image`; // Set the alt text for the image
    modal.querySelector('.modal-year').textContent = `Year: ${releaseDate}`; // Set the release year
    modal.querySelector('.modal-genre').textContent = `Genre: ${genre}`; // Set the genre
    modal.querySelector('.modal-rating').textContent = `Rating: ${rating}`; // Set the rating
    modal.querySelector('.modal-length').textContent = `Length: ${length} min`; // Set the length in minutes
    modal.querySelector('.modal-content p').textContent = description; // Set the description
    modal.querySelector('.modal-stars').textContent = `Starring: ${stars}`; // Set the stars
    modal.querySelector('#watchNowButton').href = videoUrl; // Set the link for the "Watch Now" button to the video URL

    // Store movie ID in a data attribute for later use in adding/removing the movie from the list
    modal.setAttribute('data-movie-id', videoUrl.split('/').pop());

    // Check if the movie is already in the user's list and update button accordingly
    checkMovieInList(videoUrl.split('/').pop());

    // Display the modal by changing its display style and adding a class for animation
    modal.style.display = 'block';
    setTimeout(() => {
        modal.classList.add('modal-show');
    }, 50);
}

// Function to check if the movie is in the list and update button
function checkMovieInList(movieID) {
    // Fetch the CSRF token from a hidden input in your form or meta tag
    const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

    // Make an AJAX request to check if the movie is already in the user's list
    $.ajax({
        url: "manage-movie-list/", // URL of the endpoint to check movie list
        type: "GET",
        data: {
            movie_id: movieID, // Send the movie ID to the server
        },
        success: function(data) {
            // Get the button for adding/removing the movie from the list
            const addToListButton = document.getElementById('addToListButton');
            if (data.in_list) {
                // If the movie is in the list, update button text to "Remove from List"
                addToListButton.textContent = 'Remove from List';
                addToListButton.onclick = removeItemFromList; // Set the click event to remove from the list
            } else {
                // If the movie is not in the list, update button text to "Add to List"
                addToListButton.textContent = 'Add to List';
                addToListButton.onclick = addItemToList; // Set the click event to add to the list
            }
        },
        error: function(xhr, errmsg, err) {
            // Log any errors that occur during the request
            console.error("Error checking if movie is in list: " + errmsg);
        }
    });
}

// Function to remove the selected movie from the user's list
function removeItemFromList() {
    // Get the modal element and retrieve the stored movie ID
    const modal = document.getElementById('movieModal');
    var movieID = modal.getAttribute('data-movie-id');

    if (!movieID) {
        console.error("Movie ID not found!"); // Log an error if no movie ID is found
        return;
    }

    // Fetch the CSRF token from a hidden input in your form or meta tag
    var csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

    // Make an AJAX request to remove the movie from the list
    $.ajax({
        url: "manage-movie-list/", // URL of the endpoint to remove movie from list
        type: "POST",
        data: {
            movie_id: movieID, // Send the movie ID to the server
            action: 'remove', // Specify the action as 'remove'
            csrfmiddlewaretoken: csrfToken // Include the CSRF token for security
        },
        success: function(data) {
            // Get the button for adding/removing the movie from the list
            const addToListButton = document.getElementById('addToListButton');
            if (data.status === 'success') {
                // If the movie was successfully removed, update button text to "Add to List"
                addToListButton.textContent = 'Add to List';
                addToListButton.onclick = addItemToList; // Set the click event to add to the list
                console.log(data.message); // Log success message
                location.reload(2000); // Refresh the page
            } else {
                console.error("Error: " + data.message); // Log any errors
            }
        },
        error: function(xhr, errmsg, err) {
            // Log any errors that occur during the request
            console.error("Error removing item from list: " + errmsg);
        }
    });
}

// Function to add the selected movie to the user's list
function addItemToList() {
    // Get the modal element and retrieve the stored movie ID
    const modal = document.getElementById('movieModal');
    var movieID = modal.getAttribute('data-movie-id');

    if (!movieID) {
        console.error("Movie ID not found!"); // Log an error if no movie ID is found
        return;
    }

    // Fetch the CSRF token from a hidden input in your form or meta tag
    var csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

    // Make an AJAX request to add the movie to the list
    $.ajax({
        url: "manage-movie-list/", // URL of the endpoint to add movie to list
        type: "POST",
        data: {
            movie_id: movieID, // Send the movie ID to the server
            action: 'add', // Specify the action as 'add'
            csrfmiddlewaretoken: csrfToken // Include the CSRF token for security
        },
        success: function(data) {
            // Get the button for adding/removing the movie from the list
            const addToListButton = document.getElementById('addToListButton');
            if (data.status === 'success') {
                // If the movie was successfully added, update button text to "Remove from List"
                addToListButton.textContent = data.message;
                addToListButton.onclick = removeItemFromList; // Set the click event to remove from the list
                console.log("Item added to list!"); // Log success message
                location.reload(2000); // Refresh the page
            } else {
                console.error("Error: " + data.message); // Log any errors
            }
        },
        error: function(xhr, errmsg, err) {
            // Log any errors that occur during the request
            console.error("Error adding item to list: " + errmsg);
        }
    });
}

// Function to hide the modal
function hideModal() {
    // Get the modal element
    const modal = document.getElementById('movieModal');
    modal.classList.remove('modal-show'); // Remove class that shows the modal
    setTimeout(() => {
        modal.style.display = 'none'; // Hide the modal after a delay to allow animations to complete
    }, 300);
}

// Event listener to hide the modal when clicking outside the modal content
window.onclick = function(event) {
    // Get the modal element
    const modal = document.getElementById('movieModal');
    if (event.target === modal) {
        hideModal(); // Hide the modal if clicked outside of the modal content
    }
}
