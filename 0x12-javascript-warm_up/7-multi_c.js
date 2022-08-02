#!/usr/bin/node
const process = require('process');
const args = process.argv;
const delim = parseInt(args[2]);
let i = 0;

if (isNaN(delim)) {
  console.log('Missing number of occurrences');
} else {
  while (i < delim) {
    console.log('C is fun');
    i++;
	  }
}
