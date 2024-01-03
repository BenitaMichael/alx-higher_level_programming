#!/usr/bin/node
const request = require('request');

if (process.argv.length > 2) {
  request(process.argv[2], (err, res, body) => {
    const agt = {};

    if (err) {
      console.log(err);
    }
    JSON.parse(body).forEach(element => {
      if (element.completed) {
        if (!agt[element.userId]) {
          agt[element.userId] = 0;
        }
        agt[element.userId]++;
      }
    });
    console.log(agt);
  });
}
