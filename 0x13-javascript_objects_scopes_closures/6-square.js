#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  // Method that prints the rectangle using the character c
  charPrint (c) {
    if (c === undefined) {
	  for (let i = 0; i < this.size; i++) {
	      for (let j = 0; j < this.size; j++) {
		  process.stdout.write('X');
	      }
	      console.log();
	  }
    } else {
	  for (let i = 0; i < this.size; i++) {
	      for (let j = 0; j < this.size; j++) {
		  process.stdout.write(c);
        }
        console.log();
	  }
    }
  }
}
module.exports = Square;
