#!/usr/bin/node
const request = require('request');
const { argv } = require('process');

request.get(argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    console.log(response.statusCode);
  }
});
