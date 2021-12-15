#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    /* EDGE cases */
    if (w < 1 || h < 1) { return; }
    if (w === undefined || h === undefined) { return; }

    /* values initialization */
    this.width = w;
    this.height = h;
  }
    print() {
	for (let i = 0; i < this.height; i++) {
	    for (let j = 0; j < this.width; j++) {
		process.stdout.write('X');
	    }
	    console.log();
	}
    }
}
module.exports = Rectangle;
