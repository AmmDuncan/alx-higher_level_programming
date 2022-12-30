#!/usr/bin/node
/**
 * Script to print arguments provided
 */
const argList = process.argv.slice(2);
const res = argList.join('\n');

if (!res) {
  console.log('No argument');
} else {
  console.log(res);
}
