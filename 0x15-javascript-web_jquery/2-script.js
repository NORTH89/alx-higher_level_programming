// Select the header element using the jQuery API
const header = $('header');

// Select the DIV#red_header element using the jQuery API
const redHeader = $('#red_header');

// Add a click event listener to the DIV#red_header element
redHeader.on('click', function() {
  // Update the text color of the header element to red (#FF0000)
  header.css('color', '#FF0000');
});
