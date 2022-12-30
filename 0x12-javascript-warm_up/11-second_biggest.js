#!/usr/bin/node
/**
 * find second biggest
 */

const toNumber = (v) => Number(v);
const numList = process.argv.slice(2).map(toNumber);

if ([0, 1].includes(numList.length)) {
  console.log(0);
} else {
  numList.sort((a, b) => b - a);
  console.log(numList[1]);
}
