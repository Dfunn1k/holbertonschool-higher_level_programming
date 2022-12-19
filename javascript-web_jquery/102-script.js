$(document).ready(function () {
  $('#btn_translate').click(() => {
    let code = $('#language_code').val()
    $.get(`https://stefanbohacek.com/hellosalut/?lang=${code}`, function (data) {
      $('#hello').html(data.hello)
    })
  })
});
