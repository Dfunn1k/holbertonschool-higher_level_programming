#!/usr/bin/node
const { argv } = require('process');

let numbers = [];

if ((argv[2] === undefined) || (argv.length === 3)) {
  console.log(0);
} else {
  const sliceArgumentsArgv = argv.slice(2);

  sliceArgumentsArgv.forEach((argument) => {
    numbers.push(argument);
  });

  numbers = numbers.sort(function (a, b) {
    return b - a;
  });

  console.log(numbers[1]);
}
