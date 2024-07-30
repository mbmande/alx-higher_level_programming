#!/usr/bin/env node

const axios = require('axios');
const fs = require('fs/promises');
const url = process.argv[2];
const file = process.argv[3];

const handleError = (error) => {
  console.error('Error:', error);
};

const fetchDataAndSave = async (url, file) => {
  try {
    const response = await axios.get(url);
    await fs.writeFile(file, response.data, 'utf8');
  } catch (error) {
    handleError(error);
  }
};

fetchDataAndSave(url, file);
