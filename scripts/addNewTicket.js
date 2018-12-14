"use strict";

import makeQuery from "./makeQuery.js";
import bodyControl from "./bodyControl.js";

export default function addNewTicket(request, response) {
    bodyControl(request, response, (body) => {
        const airA = parseInt(body.ticket_airport_a);
        const airB = parseInt(body.ticket_airport_b);
        const man = parseInt(body.ticket_man_id);
        const paramsArr = [
            airA,
            airB,
            man,
        ];
        makeQuery("INSERT INTO ticket (ticket_airport_a, ticket_airport_b, ticket_date, ticket_man_id) VALUES ($1, $2, NOW(), $3) RETURNING *; ", paramsArr, (arr) => {
            const result = arr[0];
            response.end(JSON.stringify(result));
        }, () => {
            response.end(JSON.stringify({
                result: "AIRPORT_OR_MAN_NOT_FOUND",
            }));
        });
    });
}
