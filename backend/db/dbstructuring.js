// include sqlite3
const sqlite3 = require('sqlite3').verbose();
const path = require('path');

const db = new sqlite3.Database(path.join(__dirname, '/app.db'));

// use db methods to create a table for media (_id, author_id, time_capsule_id, filepath)
db.run('CREATE TABLE IF NOT EXISTS media (_id INTEGER PRIMARY KEY AUTOINCREMENT, author_id INTEGER, time_capsule_id INTEGER, filepath TEXT)');

