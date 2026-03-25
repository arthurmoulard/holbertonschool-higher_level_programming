#!/usr/bin/node
const btn = document.querySelector('#update_header');

btn.addEventListener('click', function () {
  const header = document.querySelector('header');
  header.textContent = 'New Header!!!';
});