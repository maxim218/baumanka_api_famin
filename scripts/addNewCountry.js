"use strict";

import makeQuery from "./makeQuery.js";
import bodyControl from "./bodyControl";

export default function addNewCountry(request, response) {
    bodyControl(request, response, (body) => {
        makeQuery("INSERT INTO country (country_name) VALUES ($1) RETURNING *; ", [body.country_name], (arr) => {
            const result = arr[0];
            response.end(JSON.stringify(result));
        }, () => {
            response.end(JSON.stringify({
                result: "COUNTRY_ALREADY_EXISTS"
            }));
        });
    });
}

