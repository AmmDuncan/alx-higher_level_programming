#!/usr/bin/node
/**
 * calculate factorial
 */

const n = Number(process.argv[2]);

function factorial (n) {
  if ([0, 1, NaN].includes(n)) {
    return n;
  }
  return factorial(n - 1) + factorial(n - 2);
}

console.log(factorial(n));
