#!/usr/bin/node
const oldList = require('./100-data').list;
const newList = oldList.map(n => n * oldList.indexOf(n));
console.log(oldList);
console.log(newList);
