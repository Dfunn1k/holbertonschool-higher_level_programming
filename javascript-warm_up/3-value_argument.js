#!/usr/bin/node
const { argv } = require('process');

const lengthArguments = argv.length;

if (lengthArguments <= 2) {
  console.log('No argument');
} else {
  const sliceArrayArguments = argv.slice(2);

  sliceArrayArguments.forEach((argument) => {
    console.log(argument);
  });
}
