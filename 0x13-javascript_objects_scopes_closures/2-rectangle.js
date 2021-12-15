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
}
module.exports = Rectangle;
