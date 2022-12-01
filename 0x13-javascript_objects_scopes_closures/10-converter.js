#!/usr/bin/node
exports.converter = function (base) {
  return (val) => {
    function getChar (v) {
      if (v < base) {
        return '0123456789abcdefghijklmnopqrst'[v % base];
      } else {
        return getChar(Math.floor(val / base)) + '0123456789abcdefghijklmnopqrst'[v % base];
      }
    }
    return getChar(val);
  };
};
