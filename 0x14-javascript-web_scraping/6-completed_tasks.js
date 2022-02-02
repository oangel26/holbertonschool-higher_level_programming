#!/usr/bin/node
/*
script that computes the number of tasks completed by user id
*/

const args = process.argv;
const request = require('request');

request(args[2], function (err, request, body) {
  if (err) throw err;
  const data = JSON.parse(body);
  const dict = {};
  data.forEach(todos => {
    if (todos.completed) {
      if (dict[todos.userId]) {
        dict[todos.userId] += 1;
      } else {
        dict[todos.userId] = 1;
      }
    }
  });
  console.log(dict);
});
