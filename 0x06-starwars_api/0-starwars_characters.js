#!/usr/bin/node
const request = require('request');

const apiUrl = 'https://swapi-api.alx-tools.com/api/films/';

const id = process.argv[2];

function requestAsync(url) {
  return new Promise(function (resolve, reject) {
    request.get(url, function (err, res) {
      if (err) reject(err);
      resolve(res.body);
    });
  });
}

request.get(apiUrl + id, async function (err, res) {
  if (!err && res.statusCode === 200) {
    const body = JSON.parse(res.body);
    for (let i = 0; i < body.characters.length; ++i) {
      const url = body.characters[i];
      await requestAsync(url)
        .then(function (body) {
          console.log(JSON.parse(body).name);
        })
        .catch(function (err) {
          console.log(err);
        });
    }
  }
});
