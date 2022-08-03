#!/usr/bin/node
const process = require('process');
const args = process.argv;
const len = args.length;
const newArray = [];
let i = 2;

while (i < len) {
  newArray.push(args[i]);
  i++;
}

newArray.sort((a, b) => {
  return b - a;
});

console.log(newArray[1]);
