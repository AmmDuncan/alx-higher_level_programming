#!/usr/bin/node
/**
 * Script to print arguments provided
 */
for (const arg in process.argv.slice(2)) {
  console.log(arg);
}
