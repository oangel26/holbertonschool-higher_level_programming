#!/usr/bin/node
/*
Script that writes a string to file
*/

const process = require('process');
const fs = require('fs');

const args = process.argv;

try {
  fs.writeFileSync(args[2], args[3], 'utf8');
} catch (err) {
  console.error(err);
}
