#!/usr/bin/node
const converter = require('./10-converter').converter;

const myConverter = converter(2);

// for (let index = 0; index < 100; index++) {
  console.log(myConverter(10));
// }
