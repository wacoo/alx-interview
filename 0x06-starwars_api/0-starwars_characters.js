#!/usr/bin/node
/* given a movie id display one character of the movie  per line */
const request = require('request');
const arg = process.argv;
const url = 'https://swapi-api.alx-tools.com/api/films/' + arg[2];

if (arg.length > 2) {
  request.get(url, (error, _, body) => {
    if (error) {
      console.log(error);
    }
    const charURL = JSON.parse(body).characters;
    const charName = charURL.map(
      url => new Promise((resolve, reject) => {
        request(url, (err, __, charBody) => {
          if (err) {
            reject(err);
          }
          resolve(JSON.parse(charBody).name);
        });
      }));

    Promise.all(charName)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
  });
}
