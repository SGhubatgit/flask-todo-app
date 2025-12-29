// login.js
console.log("Login page JS loaded.");

// Example: focus on email input when page loads
window.onload = function() {
    const emailInput = document.querySelector('input[name="email"]');
    if(emailInput) emailInput.focus();
}
// You can add more login page specific JavaScript functionality here.