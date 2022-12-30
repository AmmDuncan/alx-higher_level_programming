#!/usr/bin/node

function addMeMaybe (n, fn) {
  fn(n + 1);
}

module.exports.addMeMaybe = addMeMaybe;
