#!/usr/bin/node
exports.esrever = function (list) {
  let i = list.length - 1;
  const reversed = [];
  while (i >= 0) {
    reversed.push(list[i]);
    i--;
  }
  return reversed;
}
;
