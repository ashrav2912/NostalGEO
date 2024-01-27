const express = require('express');
const passport = require('passport');
const Auth0Strategy = require('passport-auth0');

// Configure Passport to use Auth0
const strategy = new Auth0Strategy({
    domain: 'YOUR_AUTH0_DOMAIN',
    clientID: 'YOUR_AUTH0_CLIENT_ID',
    clientSecret: 'YOUR_AUTH0_CLIENT_SECRET',
    callbackURL: 'http://localhost:3000/callback'
}, (accessToken, refreshToken, extraParams, profile, done) => {
    // Save or retrieve user from database
    // You can customize this function to fit your needs
    // For example, you can store the user in a database or session
    // and call the done() function with the user object
    return done(null, profile);
});

passport.use(strategy);

// Serialize user object to store in session
passport.serializeUser((user, done) => {
    done(null, user);
});

// Deserialize user object from session
passport.deserializeUser((user, done) => {
    done(null, user);
});

const app = express();

// Initialize Passport and restore authentication state, if any, from the session
app.use(passport.initialize());
app.use(passport.session());

// Define routes
app.get('/', (req, res) => {
    res.send('Hello, World!');
});

app.get('/login', passport.authenticate('auth0', {
    scope: 'openid email profile'
}));

app.get('/callback', passport.authenticate('auth0', {
    failureRedirect: '/login'
}), (req, res) => {
    res.redirect('/');
});

app.get('/logout', (req, res) => {
    req.logout();
    res.redirect('/');
});

// Start the server
app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
