#!/usr/bin/node
/* Script that searches the second biggest integer in the list of arguments */

const args = process.argv;
let maxnum = 0;
let secnum = 0;
if (args.length < 3 || args.length === 3) {
  console.log(0);
} else {
  for (let i = 2; i < args.length; i++) {
    if (maxnum < args[i]) {
      maxnum = args[i];
    }
  }
  for (let j = 2; j < args.length; j++) {
    if (secnum < args[j] && args[j] !== maxnum) {
      secnum = args[j];
    }
  }
  console.log(parseInt(secnum));
}
