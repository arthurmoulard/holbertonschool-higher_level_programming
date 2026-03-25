#!/usr/bin/node
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => {
    if (!response.ok) throw new Error(`Erreur HTTP : ${response.status}`);
    return response.json();
  })
  .then(data => {
    const films = document.querySelector('#list_movies');
    data.results.forEach(film => {
      const li = document.createElement('li');
      li.textContent = film.title;
      films.appendChild(li);
    });
  });