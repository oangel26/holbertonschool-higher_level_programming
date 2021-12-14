#!/usr/bin/node
/* script that prints x times “C is fun” (x is first argument) */

const args = process.argv;

if (args[2] === undefined || isNaN(parseInt(args[2])) === true ||
    typeof parseInt(args[2]) !== 'number') {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(args[2]); i++) {
    console.log('C is fun');
  }
}
