"use strict";

import global from "./global.js";
import debug from "./debug.js";

const params = {
    database: "base",
    user: "postgres",
    password: "12345",
    host: "localhost",
    port: 5432,
};

function createNewClient() {
    const pg = global().pg;
    return new pg.Client({
        user: params.user,
        host: params.host,
        database: params.database,
        password: params.password,
        port: params.port,
    });
}

export default function makeQuery(query, arr, callbackGood, callbackBad) {
    const client = createNewClient();
    client.connect();

    if(debug() === true) {
        console.log("   ");
        console.log(query);
        console.log("----------------------------------------");
    }

    client.query(query, arr, (err, res) => {
        client.end();

        if(!err) {
            callbackGood(res.rows);
        } else {
            callbackBad();
        }
    });
}
