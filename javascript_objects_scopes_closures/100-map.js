#!/usr/bin/node
const oldList = require('./100-data').list;
const newList = oldList.map((n, i) => n * i);
console.log(oldList);
console.log(newList);
