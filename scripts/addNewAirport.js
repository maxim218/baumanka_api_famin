"use strict";

import makeQuery from "./makeQuery.js";
import bodyControl from "./bodyControl";

export default function addNewAirport(request, response) {
    bodyControl(request, response, (body) => {
        makeQuery("INSERT INTO airport (airport_name, airport_city_id) VALUES ($1, $2) RETURNING *; ", [body.airport_name, parseInt(body.airport_city_id)], (arr) => {
            const result = arr[0];
            response.end(JSON.stringify(result));
        }, () => {
            response.end(JSON.stringify({
                result: "CITY_NOT_FOUND",
            }));
        });
    });
}
