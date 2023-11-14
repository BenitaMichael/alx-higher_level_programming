#!/usr/bin/node
// script that prints x times “C is fun”

if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let j = 0; j < parseInt(process.argv[2]); j++) {
    console.log('C is fun');
  }
}