#!/usr/bin/node

const trigger = document.querySelector('#red_header');

const header = document.querySelector('header');

trigger.addEventListener('click', function () {
  header.classList.add('red');
});