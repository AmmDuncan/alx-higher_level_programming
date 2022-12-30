#!/usr/bin/node
/**
 * Script to print arguments provided
 */
const argList = process.argv.slice(2);

if (argList.length) {
  for (const arg of argList) {
    console.log(arg);
  }
} else {
  console.log('No argument');
}
