#!/usr/bin/node
const request = require('request');
const { argv } = require('process');
const newObject = {};

request.get(argv[2], (error, response, body) => {
  if (error) { console.error(error); } else {
    const dataDeserialization = JSON.parse(body);
    for (const element of dataDeserialization) {
      if (element.completed === true) {
        if (element.userId in newObject) {
          newObject[element.userId] += 1;
        } else {
          newObject[element.userId] = 1;
        }
      }
    }
    console.log(newObject);
  }
});
