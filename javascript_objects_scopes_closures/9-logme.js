#!/usr/bin/node
let storedvalue = 0;
exports.logMe = function (item){
  console.log(`${storedvalue}: ${item}`)
  storedvalue++;
}
