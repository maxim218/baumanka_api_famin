import makeQuery from "./makeQuery";

"use strict";

export default function getManInfo(request, response) {
    const id = request.params.id.toString();
    makeQuery("SELECT * FROM man INNER JOIN city ON (man_city = city_id) INNER JOIN country ON (city_country_id = country_id) WHERE man_id = $1 LIMIT 1; ", [parseInt(id)], (arr) => {
        if(arr.length === 0) {
            response.end(JSON.stringify({
                result: "MAN_NOT_EXISTS"
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
