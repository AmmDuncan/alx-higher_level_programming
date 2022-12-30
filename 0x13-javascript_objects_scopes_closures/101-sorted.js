#!/usr/bin/node

const oc = require('./101-data').dict;
const newDict = Object.entries(oc).reduce((accumDict, [id, occurrence]) => {
  const existingIds = accumDict[occurrence] || [];
  accumDict[occurrence] = [...existingIds, id];
  return accumDict;
}, {});

console.log(newDict);
