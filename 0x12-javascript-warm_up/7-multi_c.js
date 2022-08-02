#!/usr/bin/node
const process = require('process');
const args = process.argv;
const delim = args[2];
let i = 0;

while (i < delim) {
  console.log('C is fun');
  i++;
}
