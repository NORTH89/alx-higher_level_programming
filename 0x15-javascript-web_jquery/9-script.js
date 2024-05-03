// Queries an API for a translation of "hello" in French and replaces the text of the
// div#hello tag with the translation

let url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$.get(url, function (data) {
  let hello = data.translations.hello;
  $('div#hello').text(hello);
});
