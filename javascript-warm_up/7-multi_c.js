#!/usr/bin/node

const { argv } = require('process');
const times = parseInt(argv[2]);

if (isNaN(times)) {
  console.log('Missing number of ocurrences');
  return;
}

for (let i = 0; i < times; i++) {
  console.log('C is fun');
}
