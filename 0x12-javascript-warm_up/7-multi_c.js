#!/usr/bin/node

const times = process.argv[2];

if(parseInt(times)){
for(let i = 0; i < times; i++){
console.log('C is fun');}
}else if(!parseInt(times)){console.log('Missing number of times')}

