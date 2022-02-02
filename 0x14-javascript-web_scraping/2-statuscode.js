#!/usr/bin/node
/*
Script that display the status code of a GET request
*/

const args = process.argv;
const request = require('request');

request(args[2], function (err, response) {
  if (err) throw err;
  console.log('code:', response && response.statusCode);
});
