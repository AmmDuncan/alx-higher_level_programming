#!/usr/bin/node
const Square = require('./5-square.js');

module.exports = class Square extends Square {
  charPrint (c) {
    const rows = this.height;
    const cols = this.width;
    for (let i = 0; i < rows; i++) {
      console.log(Array(cols).fill(c ?? 'X').join(''));
    }
  }
};
