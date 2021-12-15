#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    /* EDGE cases */
    if (w < 1 || h < 1) {
	    return;
    }
    if (w === undefined || h === undefined) {
	    return;
    }

    /* values initialization */
    this.width = w;
    this.height = h;
  }

  // Print Method: prints the rectangle using the character X
  print () {
    for (let i = 0; i < this.height; i++) {
	    for (let j = 0; j < this.width; j++) {
        process.stdout.write('X');
	    }
	    console.log();
    }
  }

  // Rotate method: exchanges the width and the height of the rectangle
  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  // Methdo that multiples the width and the height of the rectangle by 2
  double () {
    this.width = 2 * this.width;
    this.height = 2 * this.height;
  }
}
module.exports = Rectangle;
