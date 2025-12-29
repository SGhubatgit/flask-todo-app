// dashboard.js
console.log("Dashboard page JS loaded.");

// Example: simple confirmation before deleting task
const deleteLinks = document.querySelectorAll('a[href^="/delete"]');
deleteLinks.forEach(link => {
    link.addEventListener('click', function(e){
        if(!confirm("Are you sure you want to delete this task?")){
            e.preventDefault();
        }
    });
});
// You can add more dashboard page specific JavaScript functionality here.