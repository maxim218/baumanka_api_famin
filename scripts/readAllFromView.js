"use strict";

import makeQuery from "./makeQuery";

export default function readAllFromView(request, response) {
    const v = request.params.v.toString();
    const query = "SELECT * FROM " + v + " ; " + " ";
    makeQuery(query, [], (arr) => {
        response.end(JSON.stringify(arr));
    }, () => {
        response.end(JSON.stringify({
            result: "DATABASE_ERROR",
        }));
    });
}
