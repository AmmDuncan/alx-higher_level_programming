#!/usr/bin/node
/**
 * print a square of dynamic size
 */

const size = Number(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  const row = Array(size).fill('X').join('');
  for (let i = 0; i < size; i++) {
    console.log(row);
  }
}
