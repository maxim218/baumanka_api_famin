"use strict";

import global from "./global.js";
import makeQuery from "./makeQuery.js";

export default function clear(request, response) {
    const fs = global().fs;
    const sqlCode = fs.readFileSync('main.sql', 'utf8');
    makeQuery(sqlCode.toString(), [], () => {
        response.end(JSON.stringify({
            result: "INIT_DATABASE_OK"
        }));
     }, () => {
        throw new Error();
     });
}

