#!/usr/bin/node
const { argv } = require('process');

const concatArguments = `${argv[2]} is ${argv[3]}`;
console.log(concatArguments);
