#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && Number.isInteger(w) && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i;
    const char = 'X';
    for (i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    [this.width, this.height] = [2 * this.width, 2 * this.height];
  }
}
module.exports = Rectangle;
