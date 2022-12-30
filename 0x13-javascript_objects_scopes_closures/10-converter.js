#!/usr/bin/node
exports.converter = function (base) {
  return (val) => {
    function getChar (v) {
      if (v < base) {
        return '0123456789abcdefghijklmnopqrstuvwxyz'[v % base];
      } else {
        return getChar(Math.floor(v / base)) + '0123456789abcdefghijklmnopqrstuvwxyz'[v % base];
      }
    }
    return getChar(val);
  };
};
