#!/usr/bin/node
/* script that prints a square */

const args = process.argv;

if (args.length !== 3 || isNaN(parseInt(args[2])) === true ||
    args[2] === undefined) {
  console.log('Missing size');
} else {
  for (let i = 0; i < args[2]; i++) {
    for (let j = 0; j < args[2]; j++) {
      process.stdout.write('X');
    }
    console.log();
  }
}
