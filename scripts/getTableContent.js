"use strict";

import makeQuery from "./makeQuery.js";

export default function getTableContent(request, response) {
    const tableName = request.params.table.toString();
    const idName = tableName + "_id";
    const query = " SELECT * FROM " + tableName + " ORDER BY " + idName + " DESC; ";

    makeQuery(query, [], (arr) => {
        response.end(JSON.stringify(arr));
    }, () => {
        response.end(JSON.stringify({
            result: "TABLE_NOT_FOUND",
        }));
    });
}
