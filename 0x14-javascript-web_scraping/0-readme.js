#!/usr/bin/node
/*
script that reads and prints the content of a file.
*/

const process = require('process');
const fs = require('fs');

const args = process.argv;

try {
  const data = fs.readFileSync(args[2], 'utf8');
  console.log(data);
} catch (err) {
  console.error(err);
}
