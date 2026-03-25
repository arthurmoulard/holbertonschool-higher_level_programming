#!/usr/bin/node
const btn = document.querySelector('#add_item');
const list = document.querySelector('.my_list');

btn.addEventListener('click', function () {
  const newli = document.createElement('li');
  newli.textContent = 'Item';
  list.appendChild(newli);
});