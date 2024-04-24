#!/usr/bin/node
import request from 'request';

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

async function requestPromise(url) {
  try {
    const response = await request.get(url);
    return response.body;
  } catch (error) {
    throw error;
  }
}

async function printCharacters () {
  try {
    const body = await requestPromise(url);
    const characters = JSON.parse(body).characters;

    for (let i = 0; i < characters.length; i++) {
      const characterBody = await requestPromise(characters[i]);
      console.log(JSON.parse(characterBody).name);
    }
  } catch (error) {
    console.error(error);
  }
}

printCharacters();
