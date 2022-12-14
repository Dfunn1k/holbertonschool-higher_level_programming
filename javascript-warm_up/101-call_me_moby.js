#!/usr/bin/node
exports.callMeMoby = function (num1, fn) {
  for (let i = 0; i < num1; i++) { fn(); }
};
