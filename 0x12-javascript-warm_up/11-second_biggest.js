#!/usr/bin/node
const process = require('process');
const args = process.argv;
const len = args.length;
const newArray = [];
let i = 2;

if (args[2] === undefined) {
  console.log(0);
} else if (len === 3) {
  console.log(0);
} else {
  while (i < len) {
    newArray.push(args[i]);
    i++;
  }
  newArray.sort((a, b) => {
    return b - a;
  });
  console.log(newArray[1]);
}
