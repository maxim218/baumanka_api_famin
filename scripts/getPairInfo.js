"use strict";

import makeQuery from "./makeQuery";

export default function getPairInfo(request, response) {
    const id = request.params.id.toString();
    makeQuery("SELECT pair_id, pair_man_a, pair_man_b, m1.man_fullname AS man_1, m2.man_fullname AS man_2 FROM pair INNER JOIN man AS m1 ON (pair_man_a = m1.man_id) INNER JOIN man AS m2 ON (pair_man_b = m2.man_id) WHERE pair_id = $1 LIMIT 1; ", [parseInt(id)], (arr) => {
        if(arr.length === 0) {
            response.end(JSON.stringify({
                result: "PAIR_NOT_FOUND"
            }));
        } else {
            const result = arr[0];
            response.end(JSON.stringify(result));
        }
    }, () => {
        response.end(JSON.stringify({
            result: "DATABASE_ERROR",
        }));
    });
}
