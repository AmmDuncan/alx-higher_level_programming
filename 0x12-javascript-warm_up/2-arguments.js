#!/usr/bin/node
const args = process.argv;
if (!args || args.length <= 2) console.log('No argument');
if (args && args.length === 3) console.log('Argument found');
if (args && args.length > 3) console.log('Arguments found');
