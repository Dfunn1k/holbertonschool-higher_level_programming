#!/usr/bin/node
const { argv } = require('process');

function factorialRecursive (num1) {
  if (isNaN(num1)) {
    num1 = 1;
  }
  if (num1 === 1) {
    return 1;
  } else {
    return num1 * factorialRecursive(num1 - 1);
  }
}

const number = parseInt(argv[2]);
const result = factorialRecursive(number);
console.log(result);
