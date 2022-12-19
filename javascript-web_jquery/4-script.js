$('#toggle_header').click(() => {
  const valueClass = $('header').attr('class');
  if (valueClass === 'green') {
    $('header').attr('class', 'red');
  } else {
    $('header').attr('class', 'green');
  }
});
