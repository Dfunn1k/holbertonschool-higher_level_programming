#!/usr/bin/node

const { argv } = require('process');
const lenArguments = argv.length;

if (lenArguments <= 2) {
  console.log('No argument');
} else if (lenArguments === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
