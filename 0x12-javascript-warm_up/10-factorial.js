#!/usr/bin/node
/**
 * calculate factorial
 */

const n = Number(process.argv[2]);

function factorial (n) {
  if ([0, 1, NaN].includes(n)) {
    return 1;
  }
  return n * factorial(n - 1);
}

console.log(factorial(n));
