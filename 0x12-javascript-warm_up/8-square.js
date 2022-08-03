#!/usr/bin/node
const process = require('process');
const args = process.argv;
const size = parseInt(args[2]);
let i; const char = 'X';

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (i = 0; i < size; i++) {
    console.log(char.repeat(size));
  }
}
