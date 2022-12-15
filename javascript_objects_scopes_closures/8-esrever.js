#!/usr/bin/node
exports.esrever = function (list) {
  const lenList = list.length;
  const newList = [];

  for (let i = lenList - 1; i >= 0; i--) {
    newList.push(list[i]);
  }
  return newList;
};
