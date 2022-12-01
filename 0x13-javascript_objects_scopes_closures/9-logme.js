#!/usr/bin/node
exports.logMe = function logMe (item) {
  const count = logMe.count || 0;
  console.log(`${count}: ${item}`);
  logMe.count = count + 1;
};
