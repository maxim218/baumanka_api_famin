"use strict";

import makeQuery from "./makeQuery.js";
import bodyControl from "./bodyControl";

export default function addNewCity(request, response) {
    bodyControl(request, response, (body) => {
        makeQuery("INSERT INTO city (city_name, city_country_id) VALUES($1, $2) RETURNING *; ", [body.city_name, parseInt(body.city_country_id)], (arr) => {
            const result = arr[0];
            response.end(JSON.stringify(result));
        }, () => {
            response.end(JSON.stringify({
                result: "COUNTRY_NOT_FOUND",
            }));
        });
    });
}
