#!/usr/bin/node
exports.nbOccurences = function (list, searchElemenet) {
  let o = 0;
  list.forEach(item => {
    if (item === searchElemenet) o++;
  });
  return o;
};
