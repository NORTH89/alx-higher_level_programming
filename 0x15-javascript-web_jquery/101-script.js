// Adds a new item to the list when the user clicks on the "Add item" button
$('#add_item').click(function () {
  $('ul.my_list').append('<li>Item</li>');
});

// Removes the last item from the list when the user clicks on the "Remove item" button
$('#remove_item').click(function () {
  $('ul.my_list li:last-child').remove();
});

// Clears all items from the list when the user clicks on the "Clear list" button
$('#clear_list').click(function () {
  $('ul.my_list').empty();
});
