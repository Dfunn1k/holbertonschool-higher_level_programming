#!/usr/bin/node
exports.esrever = (list) => {
  const newList = [];
  const len = list.length;
  let i;
  while (len) {
    newList.push(list.pop());
  }
  return (newList);
};
