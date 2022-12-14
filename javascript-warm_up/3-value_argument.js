#!/usr/bin/node
const { argv } = require('process');

if (argv[2] === undefined) {
  console.log('No argument');
} else {
  const sliceArrayArguments = argv.slice(2);

  sliceArrayArguments.forEach((argument) => {
    console.log(argument);
  });
}
