#!/usr/bin/node
/**
 * add two numbers
 */

function add(a, b) {
  return a + b;
}

const [a, b] = process.argv.slice(2).map(n => Number(n));
console.log(add(a, b));