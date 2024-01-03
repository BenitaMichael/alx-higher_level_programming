#!/usr/bin/node
const request = require('request');

if (process.argv.length > 2) {
  request(`${process.argv[2]}`, (err, res, body) => {
    if (err) {
      console.log(err);
    } else if (body) {
      const targetFilms = JSON.parse(body).results.filter(
        x => x.characters.find(y => y.match(/\/people\/18\/?$/))
      );

      console.log(targetFilms.length);
    }
  });
}

