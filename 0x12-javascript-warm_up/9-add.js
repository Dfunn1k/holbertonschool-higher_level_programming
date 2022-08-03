#!/usr/bin/node
const process = require('process');
const args = process.argv;

function add (a, b) {
  return parseInt(a) + parseInt(b);
}

console.log(add(args[2], args[3]));
