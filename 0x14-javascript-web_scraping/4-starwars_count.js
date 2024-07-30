#!/usr/bin/env node

const request = require('request');
const url = process.argv[2];
const characterId = '18';
let count = 0;

const handleError = (error) => {
  console.log(error);
};

const processData = (body) => {
  const data = JSON.parse(body);
  data.results.forEach((film) => {
    film.characters.forEach((character) => {
      if (character.includes(characterId)) {
        count += 1;
      }
    });
  });
  console.log(count);
};

request.get(url, (error, response, body) => {
  if (error) {
    handleError(error);
  } else {
    processData(body);
  }
});

