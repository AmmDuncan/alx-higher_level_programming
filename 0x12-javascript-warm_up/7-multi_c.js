#!/usr/bin/node
/*
 * print "C is fun" number of times provided
 */

const times = process.argv[2];
let i = 0;

while (i < times) {
 console.log('C is fun');
 i++;
}
