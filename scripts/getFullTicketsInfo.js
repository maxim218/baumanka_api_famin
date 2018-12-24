"use strict";

import makeQuery from "./makeQuery";

export default function getFullTicketsInfo(request, response) {
    let query = "SELECT ticket_id, man_fullname, a1.airport_name AS air_1, a2.airport_name AS air_2 FROM ticket ";
    query += "INNER JOIN airport AS a1 ON (ticket_airport_a = a1.airport_id) ";
    query += "INNER JOIN airport AS a2 ON (ticket_airport_b = a2.airport_id) ";
    query += "INNER JOIN man ON (man_id = ticket_man_id) ";
    query += "ORDER BY ticket_id DESC; ";

    makeQuery(query, [], (arr) => {
        response.end(JSON.stringify(arr));
    }, () => {
        response.end(JSON.stringify({
            result: "DATABASE_ERROR",
        }));
    });
}
