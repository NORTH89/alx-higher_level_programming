// Queries an API for a translation of "hello" in the specified 
// language and replaces the text of the
// div#hello tag with the translation

$('#btn_translate').click(function () {
  let languageCode = $('#language_code').val();
  let url = `https://www.fourtonfish.com/hellosalut/hello/${languageCode}`;
  $.get(url, function (data) {
	let hello = data.hello;
	$('div#hello').text(hello);
  });
});
