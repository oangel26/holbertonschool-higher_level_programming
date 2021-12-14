#!/usr/bin/node
/* prints My number: <#> if the first argument can be converted to an integer */

const args = process.argv;
if (args[2] === undefined) {
  console.log('Not a number');
} else if (typeof args[2] === 'undefined') {
  console.log('Not a number');
} else if (isNaN(parseInt(args[2])) === true) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(args[2]));
}
