#!/usr/bin/node
const request = require('request');
const { argv } = require('process');
let count = 0;

request.get(argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const dataDeserialization = JSON.parse(response.body);
    for (const film of dataDeserialization.results) {
      for (const peopleFilm of film.characters) { if (peopleFilm.includes('18')) { count++; } }
    }
    console.log(count);
  }
});
