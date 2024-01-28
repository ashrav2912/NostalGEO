const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const multer = require('multer'); // For handling file uploads
const path = require('path');
const app = express();
const port = 3000;
const db = new sqlite3.Database(path.join(__dirname, '/db/app.db'));


// Configure multer to handle file uploads
const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        cb(null, path.join(__dirname, '/uploads/')); // Set the destination folder
    },
    filename: (req, file, cb) => {
        // Generate a unique filename
        const uniqueName = Date.now() + '-' + Math.round(Math.random() * 1E9) + path.extname(file.originalname);
        cb(null, uniqueName);
    }
});

const upload = multer({ storage });


// db.run("DELETE FROM markers"); // UNCOMMENT/COMMENT OUT THIS LINE IF YOU WANT TO CLEAR/PRESERVE THE TABLE FULL OF MARKERS. RESTART THE SERVER FOR THIS TO TAKE EFFECT

// EXPECTS LOCATION PARAMETER. PASS AS lat=123.123,long=123.123
app.get('/create_marker', (req, res) => {
    db.run('INSERT INTO markers (lat, long) VALUES (?, ?)', [req.query.lat, req.query.long], function(err) {
        if (err) {
            return console.log(err.message);
        }
        res.send(`A row has been inserted with rowid ${this.lastID}`);
    });
});

// NO PARAMETERS REQUIRED. RETURNS ALL MARKERS.
app.get('/get_markers', (req, res) => {
    db.all('SELECT * FROM markers', [], (err, rows) => {
        if (err) {
            throw err;
        }
        // console.log(JSON.stringify(rows));
        res.send(rows);

    });
});



// EXPECTS LATITUDE AND LONGITUDE TO BE PASSED AS lat = 123.123 AND long = 123.123, AND DATE TO BE PASSED AS date = (any string)
app.get('/create_time_capsule', (req, res) => {
    // where lat and long are within 0.001 of the new marker about to be created, then return the id of that marker
    db.all('SELECT * FROM markers WHERE lat BETWEEN ? AND ? AND long BETWEEN ? AND ?', [req.query.lat - 0.001, req.query.lat + 0.001, req.query.long - 0.001, req.query.long + 0.001], (err, rows) => {
        if (err) {
            throw err;
        }
        if (rows.length == 0) {
            db.get('INSERT INTO markers (lat, long) VALUES (?, ?) RETURNING *', [req.query.lat, req.query.long], function(err, result) {
                if(err) throw err;
                db.run('INSERT INTO time_capsules (author_id, marker_id, date) VALUES (1, ?, ?)', [result._id, req.query.date], function(err) {
                    if (err) {
                        return console.log(err.message);
                    }
                    res.send(`A row has been inserted with rowid ${this.lastID}`);
                });
            });
        } else {
            db.get('INSERT INTO time_capsules (author_id, marker_id, date) VALUES (1, ?, ?)', [rows[0]._id, req.query.date], function(err, inserted) {
                if (err) {
                    return console.log(err.message);
                }
                res.send(`A row has been inserted with rowid ${inserted}`);
            });
        }
        
    });
});


// EXPECTS A MARKER ID TO BE PASSED AS marker_id = 123
app.get('/get_time_capsules', (req, res) => {
    db.all('SELECT * FROM time_capsules WHERE marker_id = ?', [req.query.marker_id], (err, rows) => {
        if (err) {
            throw err;
        }
        res.send(rows);
    });
})




// ADDING FILES
app.post('/upload', upload.array('file'), (req, res) => {
    // console.log(req.files);
    res.send('Files uploaded successfully');
});

    





app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
