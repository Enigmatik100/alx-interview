#!/usr/bin/node

const request = require('request');
const id = parseInt(process.argv[2]);
const URL = `https://swapi-api.alx-tools.com/api/films/${id}/`;
request(URL, { json: true }, async (err, res, body) => {
  if (err) console.log(err);
  const characters = body.characters;
  for (const charUrl of characters) {
    await new Promise((resolve, reject, body) => {
      request(charUrl, { json: true }, (error, response, responseBody) => {
        if (error) reject(err);
        resolve(responseBody);
        console.log(responseBody.name);
      });
    });
  }
});
