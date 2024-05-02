// Select the header element using the jQuery API
const header = $('header');

// Select the DIV#red_header element using the jQuery API
const redHeader = $('#red_header');

// Add a click event listener to the DIV#red_header element
redHeader.on('click', function() {
  // Add the class red to the header element
  header.addClass('red');
});
