#!/usr/bin/node
/*
Script that prints the number of movies where the
character “Wedge Antilles” is present.
*/

const args = process.argv;
const request = require('request');

let count = 0;
request(args[2], function (err, request) {
  if (err) throw err;
  const data = JSON.parse(request.body);
  data.results.forEach(movieList => {
    movieList.characters.forEach(characterList => {
      const url = characterList;
      if (url.indexOf('18') !== -1) { count++; }
    });
  });
  console.log(count);
});
