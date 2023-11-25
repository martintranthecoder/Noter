document.addEventListener('DOMContentLoaded', function() {

    // Example: Autosave functionality
    const saveInterval = 30000; // Autosave every 30 seconds
    let titleInput = document.getElementById('title');
    let contentInput = document.getElementById('content');
    let noteId = document.getElementById('note-id').value; // Assuming you have a hidden input for note ID

    // Function to autosave note data
    function autosaveNote() {
        let title = titleInput.value;
        let content = contentInput.value;

        // Make an AJAX request to your Flask route for saving the note
        fetch('/save-note/' + noteId, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ title: title, content: content })
        })
        .then(response => response.json())
        .then(data => {
            console.log('Note autosaved:', data.message);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    }

    // Set interval for autosaving
    setInterval(autosaveNote, saveInterval);

    // Additional JavaScript for editing functionalities can go here

});
