const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const path = require('path');
const app = express();
const port = 3000;
const db = new sqlite3.Database(path.join(__dirname, '/db/app.db'));

app.get('/create_marker', (req, res) => {
    const lat = req.query.location.split(',')[0];
    const long = req.query.location.split(',')[1];
    db.run('INSERT INTO markers (_id, lat, long) VALUES (?, ?)', [lat, long], function(err) {
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
        console.log(JSON.stringify(rows));
        res.send(rows);

    });
});



app.get('/create_time_capsule', (req, res) => {
    db.run('INSERT INTO time_capsules (_id, author_id, marker_id, date) VALUES (?, 1, ?,)', [req.query.location, req.query.date, req.query.message], function(err) {
        if (err) {
            return console.log(err.message);
        }
        res.send(`A row has been inserted with rowid ${this.lastID}`);
    });
});



app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
