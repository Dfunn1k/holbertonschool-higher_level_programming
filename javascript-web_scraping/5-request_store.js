#!/usr/bin/node
const request = require('request');
const { argv } = require('process');
const fs = require('fs');

request.get(argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFileSync(argv[3], body);
  }
});
