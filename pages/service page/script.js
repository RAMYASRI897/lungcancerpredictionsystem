document.getElementById('contactForm').addEventListener('submit', function (e) {
  let valid = true;

  const name = document.getElementById('name');
  const email = document.getElementById('email');
  const message = document.getElementById('message');

  const nameError = document.getElementById('nameError');
  const emailError = document.getElementById('emailError');
  const messageError = document.getElementById('messageError');

  nameError.style.display = emailError.style.display = messageError.style.display = 'none';

  if (name.value.trim() === '') {
    nameError.textContent = 'Please enter your name.';
    nameError.style.display = 'block';
    valid = false;
  }

  if (!email.value.match(/^\S+@\S+\.\S+$/)) {
    emailError.textContent = 'Enter a valid email.';
    emailError.style.display = 'block';
    valid = false;
  }

  if (message.value.trim().length < 10) {
    messageError.textContent = 'Message must be at least 10 characters.';
    messageError.style.display = 'block';
    valid = false;
  }

  if (!valid) e.preventDefault();
});
