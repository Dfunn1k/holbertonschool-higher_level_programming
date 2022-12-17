#!/usr/bin/node
const request = require('request');
const { argv } = require('process');

request.get(`https://swapi-api.hbtn.io/api/films/${argv[2]}/`, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const tittle = JSON.parse(response.body);
    console.log(tittle.title);
  }
});
