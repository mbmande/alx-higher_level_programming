#!/usr/bin/node

const argc = process.argv.length;

argc > 2 ? console.log(`Argument${(argc > 3 ? 's ' : '')}found`) : console.log('No arguemt');

