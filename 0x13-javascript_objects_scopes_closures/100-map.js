#!/usr/bin/node

const list = require('./100-data').list;
const toProductOfIndex = (num, index) => num * index;
const newList = list.map(toProductOfIndex)
console.log(list);
console.log(newList);
