#!/usr/bin/node
/*
that gets the contents of a webpage and stores it in a file.
*/

const args = process.argv;
const request = require('request');

request(args[2], function (err, request) {
  if (err) throw err;
  const data = JSON.parse(request.body);
  const fs = require('fs');
  try {
    fs.writeFileSync(args[3], data, 'utf8');
  } catch (err) {
    console.error(err);
  }
});
