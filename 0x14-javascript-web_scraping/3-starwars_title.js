#!/usr/bin/node
/*
Script that prints the title of a Star Wars movie where the episode
number matches a given integer.
*/

const args = process.argv;
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/'

const data = request(url + args[2], function (err, response) {
  if (err) throw err;
});

console.log(data.title)
