#!/usr/bin/node
const { argv } = require('node:process');

let x = argv[2];

if (!Number(x) || Number(x) === 0) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < Number(x); i++) {
    console.log('C is fun');
  }
}
