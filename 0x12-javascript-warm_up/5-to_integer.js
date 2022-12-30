#!/usr/bin/node
/*
 * convert number to integer
 */

const arg = process.argv[2];

const argAsNum = Number(arg);

if (Number.isNaN(argAsNum)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${argAsNum}`);
}
