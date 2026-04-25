/* global $ */
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  data.results.forEach(function (film) {
    $('ul#list_movies').append('<li>' + film.title + '</li>');
  });
});
