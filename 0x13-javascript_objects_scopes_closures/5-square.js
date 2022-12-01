#!/usr/bin/node
import Rectangle from './4-rectangle';

export class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
