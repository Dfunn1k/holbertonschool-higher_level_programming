#!/usr/bin/node
const process = require('process');
const args = process.argv;
const number = parseInt(args[2]);

function factorial (number) {
  if (number === 1) {
    return 1;
  } else {
    return number * factorial(number - 1);
  }
}

if (isNaN(number)) {
  console.log(1);
} else {
  console.log(factorial(number));
}
