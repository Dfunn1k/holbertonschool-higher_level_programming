#!/usr/bin/node
exports.esrever = function (list) {
  const newArray = [];
  list.forEach((item) => newArray.unshift(item));
  return (newArray);
};
