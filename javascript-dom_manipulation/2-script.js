#!/usr/bin/node

const btn = document.querySelector('#red_header');

const header = document.querySelector('header');

btn.addEventListener('click', function () {
  header.classList.add('red');
});