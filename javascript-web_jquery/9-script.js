$(document).ready(function() {
  $.get('https://stefanbohacek.com/hellosalut/?lang=fr', function(data) {
    $('#hello').html(data.hello)
});
});
