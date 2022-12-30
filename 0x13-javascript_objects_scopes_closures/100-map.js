#!/usr/bin/node

const list = require('100-data.js').list;

const toProductOfIndex = (num, index) => num * index;
console.log(list);
console.log(list.map(toProductOfIndex));
