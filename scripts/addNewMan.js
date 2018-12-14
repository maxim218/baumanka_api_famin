"use strict";

import makeQuery from "./makeQuery.js";
import bodyControl from "./bodyControl";

export default function addNewMan(request, response) {
    bodyControl(request, response, (body) => {
        makeQuery("INSERT INTO man (man_fullname, man_city) VALUES ($1, $2) RETURNING *; ", [body.man_fullname, parseInt(body.man_city)], (arr) => {
            const answer = arr[0];
            response.end(JSON.stringify(answer));
        }, () => {
            response.end(JSON.stringify({
                result: "CITY_NOT_FOUND",
            }));
        });
    });
}
