function checkFormCompletion() {
  var form = document.querySelector('form');
  var isFormComplete = true;
  console.log('checking form completion');
  form.querySelectorAll('input, textarea').forEach(function (element) {
    if (element.hasAttribute('required') && element.value === '') {
      isFormComplete = false;
      console.log(element.name + ' is empty');
    }
  });

  if (isFormComplete && isCaptchaPassed) {
    form.querySelector('input[type=submit]').disabled = false;
  } else {
    form.querySelector('input[type=submit]').disabled = true;
  }
}

document.querySelectorAll('input, textarea').forEach(function (element) {
  element.addEventListener('input', checkFormCompletion);
});

var isCaptchaPassed = false;
function captchaPassed(response) {
  isCaptchaPassed = true;
  checkFormCompletion();
  console.log(response);
  return response;
}
