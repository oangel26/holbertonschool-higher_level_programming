#!/usr/bin/node
/*
Script that prints the number of movies where the
character “Wedge Antilles” is present.
*/

const args = process.argv;
const request = require('request');

let count = 0;
request(args[2] + , function (err, request) {
  if (err) throw err;
  const data = JSON.parse(request.body);
    for (let film in data.results) {
	for (let character in film.characters) {
	    if (character === "https://swapi-api.hbtn.io/api/people/18/") {
		count++;
	    }
	}
    }
    console.log(count);
});
