"use strict";

import makeQuery from "./makeQuery";

export default function getCountryByCityName(request, response) {
    const dictionary = request.query;
    const name = dictionary["name"];
    makeQuery("SELECT * FROM city INNER JOIN country ON (city_country_id = country_id) WHERE city_name = $1 LIMIT 1; ", [name], (arr) => {
        if(arr.length === 0) {
            response.end(JSON.stringify({
                result: "NOT_FOUND"
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
