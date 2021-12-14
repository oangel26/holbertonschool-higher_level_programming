#!/usr/bin/node
/* script that computes and prints a factorial */

function factorial (n) {
  if (n === undefined) {
    return (1);
  } else if (n === 0) {
    return (1);
  } else {
    return (n * factorial(n - 1));
  }
}
const args = process.argv;

const result = factorial(args[2]);
console.log(result);
