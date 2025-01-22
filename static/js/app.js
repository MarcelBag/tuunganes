console.log('Welcome to Tuunganes Website!');
const subscribeForm = document.getElementById('subscribeForm');

subscribeForm.addEventListener('submit', async (e) => {
    e.preventDefault(); // Prevent the form from reloading the page

    const formData = new FormData(subscribeForm);
    const response = await fetch('/subscribe', {
        method: 'POST',
        body: formData,
    });

    const result = await response.json();
    if (response.ok) {
        alert(result.message); // Show success message
        subscribeForm.reset(); // Clear the form
    } else {
        alert(result.error); // Show error message
    }
});
