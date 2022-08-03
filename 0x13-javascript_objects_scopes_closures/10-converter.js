#!/usr/bin/node
exports.converter = function (base) {
  return (number) => Number(number).toString(base);
};
