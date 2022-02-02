#!/usr/bin/node
/*
Script that prints the title of a Star Wars movie where the episode
number matches a given integer.
*/

const args = process.argv;
const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + args[2], function (err, request) {
  if (err) throw err;
  const data = JSON.parse(request.body);
  console.log(data['title']);
});
