#!/usr/bin/node
/*
Script that display the status code of a GET request
*/

const process = require('process');
const args = process.argv;

const requestURL = args[2];

const request = require('request');
request(requestURL, function (response) {
  console.log('statusCode:', response.statusCode);
});
