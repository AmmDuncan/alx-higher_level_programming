#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const rows = this.height;
    const cols = this.width;

    for (let i = 0; i < rows; i++) {
      console.log(Array(cols).fill('X').join(''));
    }
  }
};
