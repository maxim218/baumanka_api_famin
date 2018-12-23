"use strict";

import makeQuery from "./makeQuery.js";
import bodyControl from "./bodyControl";

export default function addPair(request, response) {
    bodyControl(request, response, (body) => {
        const a = parseInt(body.pair_man_a);
        const b = parseInt(body.pair_man_b);
        makeQuery("INSERT INTO pair (pair_man_a, pair_man_b) VALUES ($1, $2) RETURNING *; ", [a, b], (arr) => {
            const result = arr[0];
            response.end(JSON.stringify(result));
        }, () => {
            response.end(JSON.stringify({
                result: "MAN_NOT_FOUND",
            }));
        });
    });
}
