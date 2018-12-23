"use script";

import global from "./global.js";
import route from "./route.js";
import generate from "./generate.js";

const PORT = 5007;

function start() {
    let express = require("express");
    let app = express();

    let pg = require('pg');
    global().pg = pg;

    let fs = require('fs');
    global().fs = fs;

    app.use(function(req, res, next) {
        res.header("Cache-Control", "no-cache, no-store, must-revalidate");
        res.header("Access-Control-Allow-Origin", "*");
        res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
        next();
    });

    const port = parseInt(PORT);
    app.listen(port);
    console.log("    ");
    console.log("Server port: " + port);
    console.log("-----------------------------------");
    console.log("    ");

    generate("addCountry", ['country_name'], 'api/database/country/add');
    generate("addCity", ['city_name', 'city_country_id'], 'api/database/city/add');
    generate("addAirport", ['airport_name', 'airport_city_id'], 'api/database/airport/add');
    generate("addMan", ['man_fullname', 'man_city'], 'api/database/man/add');
    generate("addTicket", ['ticket_airport_a', 'ticket_airport_b', 'ticket_man_id'], 'api/database/ticket/add');
    generate("addPair", ["pair_man_a", "pair_man_b"], 'api/database/pair/add');

    route(app);
}

start();

function printNewLines() {
    console.log("    ");
    console.log("-----------------------------------");
    console.log("    ");
    console.log("System is ready to work ...");
    console.log("    ");
}

setTimeout(printNewLines, 4000);