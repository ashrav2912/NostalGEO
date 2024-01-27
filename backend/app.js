const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const app = express();
const port = 3000;
const db = new sqlite3.Database('.db/app.db');

app.get('/create_marker', (req, res) => {
    db.run('INSERT INTO markers (location) VALUES (?)', [req.query.location], function(err) {
        if (err) {
            return console.log(err.message);
        }
        res.send(`A row has been inserted with rowid ${this.lastID}`);
    });
});

app.get('/get_markers', (req, res) => {
    db.all('SELECT * FROM markers', [], (err, rows) => {
        if (err) {
            throw err;
        }
        res.send(rows);
    });
});




app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
