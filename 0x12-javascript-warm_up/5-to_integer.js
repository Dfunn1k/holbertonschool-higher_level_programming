#!/usr/bin/node
const process = require('process');
const args = process.argv;
const argconvert = parseInt(args[2]);

if (isNaN(argconvert)) {
	console.log('Not a number')
} else {
	console.log(`My number: ${argconvert}`)
}
