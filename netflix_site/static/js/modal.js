// Function to show the modal with movie details
function showModal(element) {
    // Find the closest parent element with the class 'banner-slide' or 'movie-thumbnail'
    const parent = element.closest('.banner-slide, .movie-thumbnail');

    // Retrieve the movie details from data attributes
    const title = parent.getAttribute('data-title'); // Get the movie title
    const description = parent.getAttribute('data-description'); // Get the movie description
    const releaseDate = parent.getAttribute('data-release-date'); // Get the release date
    const genre = parent.getAttribute('data-genre'); // Get the genre
    const length = parent.getAttribute('data-length'); // Get the movie length
    const imageCoverUrl = parent.getAttribute('data-image-cover-url'); // Get the URL for the cover image
    const videoUrl = parent.getAttribute('data-video-url'); // Get the URL for the video

    // Get the modal element by its ID
    const modal = document.getElementById('movieModal');

    // Update the modal's content with the movie details
    modal.querySelector('.modal-header h2').textContent = title; // Set the title in the modal header
    modal.querySelector('.modal-image').src = imageCoverUrl; // Set the cover image source
    modal.querySelector('.modal-image').alt = `${title} Cover Image`; // Set the alt text for the image
    modal.querySelector('.modal-year').textContent = `Year: ${releaseDate}`; // Set the release year
    modal.querySelector('.modal-genre').textContent = `Genre: ${genre}`; // Set the genre
    modal.querySelector('.modal-length').textContent = `Length: ${length} min`; // Set the length in minutes
    modal.querySelector('.modal-content p').textContent = description; // Set the description
    modal.querySelector('#watchNowButton').href = videoUrl; // Set the link for the "Watch Now" button to the video URL

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
