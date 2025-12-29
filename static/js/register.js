// register.js
console.log("Register page JS loaded.");

// Example: simple password match alert
const form = document.querySelector('form');
if(form) {
    form.addEventListener('submit', function(e){
        const pwd = form.querySelector('input[name="password"]').value;
        const confirm = form.querySelector('input[name="confirm_password"]').value;
        if(pwd !== confirm){
            e.preventDefault();
            alert("Passwords do not match!");
        }
    });
}
// You can add more register page specific JavaScript functionality here.