#!/usr/bin/node

function callMeMoby (times, fn) {
  for (let i = 0; i < times; i++) {
    fn();
  }
}

exports.callMeMoby = callMeMoby;
