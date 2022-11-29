#!/usr/bin/node
const args = process.argv;
if (args.length === 1) console.log('No argument');
if (args.length === 2) console.log('Argument found');
if (args.length > 2) console.log('Arguments found');