#!/usr/bin/node
// prints a square

if (isNaN(process.argv[2])) {
    console.log('Missing size');
  } else {
    for (let j = 0; j < parseInt(process.argv[2]); j++) {
      console.log('X'.repeat(parseInt(process.argv[2])));
    }
  }