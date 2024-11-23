document.getElementById('editButton').addEventListener('click', function() {
    const inputs = document.querySelectorAll('#profileForm input, #profileForm textarea');
    const saveButton = document.getElementById('saveButton');
    const editButton = document.getElementById('editButton');
    const profileContainer = document.querySelector('.profile-container');
    const formGroups = document.querySelectorAll('.form-group label');
    
    inputs.forEach(input => {
        input.disabled = !input.disabled;
    });
    
    if (editButton.innerText === "Edit") {
        editButton.innerText = "Cancel";
        saveButton.style.display = "inline-block";
        profileContainer.classList.add('edit-mode');
    } else {
        editButton.innerText = "Edit";
        saveButton.style.display = "none";
        profileContainer.classList.remove('edit-mode');
    }
});

document.getElementById('profileForm').addEventListener('submit', function(e) {
    e.preventDefault();
    // Handle form submission, like sending data to the server

    // Disable inputs after saving
    const inputs = document.querySelectorAll('#profileForm input, #profileForm textarea');
    inputs.forEach(input => {
        input.disabled = true;
    });

    // Reset buttons and effects
    document.getElementById('editButton').innerText = "Edit";
    document.getElementById('saveButton').style.display = "none";
    document.querySelector('.profile-container').classList.remove('edit-mode');
});
function enableEdit() {
    const inputs = document.querySelectorAll('input');
    inputs.forEach(input => input.disabled = false);

    // Add black backlight effect to the entire profile container
    const profileContainer = document.querySelector('.profile-container');
    profileContainer.classList.add('black-backlight');
}
window.addEventListener('load', () => {
    const fadeInElements = document.querySelectorAll('.fade-in');
    fadeInElements.forEach(element => {
        element.classList.add('visible');
    });
});

