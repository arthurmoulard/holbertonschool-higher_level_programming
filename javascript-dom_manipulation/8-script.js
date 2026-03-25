#!/usr/bin/node
document.addEventListener('DOMContentLoaded', function () {
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(response => {
      if (!response.ok) throw new Error(`Erreur HTTP : ${response.status}`);
      return response.json();
    })
    .then(data => {
      const hello = document.querySelector('#hello');
      hello.textContent = data.hello;
    });
});