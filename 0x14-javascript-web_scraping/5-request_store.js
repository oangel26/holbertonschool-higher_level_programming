#!/usr/bin/node
/*
that gets the contents of a webpage and stores it in a file.
*/

const args = process.argv;
const request = require('request');
const fs = require('fs');

request(args[2]).pipe(fs.createWriteStream(args[3]));
