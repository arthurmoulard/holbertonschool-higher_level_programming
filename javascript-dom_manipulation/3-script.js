#!/usr/bin/node
const header = document.querySelector('header');
const btn = document.querySelector('#toggle_header');

btn.addEventListener('click', function () {
  if (header.classList.contains('red')) {
    header.classList.remove('red');
    header.classList.add('green');
  } else {
    header.classList.remove('green');
    header.classList.add('red');
  }
});