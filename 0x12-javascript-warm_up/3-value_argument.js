#!/usr/bin/node
/**
 * Script to print arguments provided
 */
for (const arg of process.argv.slice(2)) {
  console.log(arg);
}
