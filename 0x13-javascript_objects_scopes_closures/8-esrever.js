#!/usr/bin/node
exports.esrever = (list) => {
  const newList = [];
  const len = list.length;
  let i;
  while (i < len) {
    newList.push(list.pop());
    i++;
  }
  return (newList);
};
