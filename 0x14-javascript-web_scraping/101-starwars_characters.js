#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

function getCharacters(url) {
  return new Promise((resolve, reject) => {
    request.get(url, (error, response, body) => {
      if (error) reject(error);
      else {
        const data = JSON.parse(body);
        const characters = data.characters;
        resolve(characters);
      }
    });
  });
}

async function printCharacters(characters) {
  for (const character of characters) {
    const characterData = await getCharacter(character);
    console.log(characterData.name);
  }
}

function getCharacter(url) {
  return new Promise((resolve, reject) => {
    request.get(url, (error, response, body) => {
      if (error) reject(error);
      else {
        const data = JSON.parse(body);
        resolve(data);
      }
    });
  });
}

getCharacters(url)
  .then(characters => printCharacters(characters))
  .catch(error => console.error(error));
