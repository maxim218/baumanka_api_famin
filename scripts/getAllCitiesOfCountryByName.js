"use strict";

import makeQuery from "./makeQuery";

export default function getAllCitiesOfCountryByName(request, response) {
    const dictionary = request.query;
    const name = dictionary["name"];
    makeQuery("SELECT * FROM country INNER JOIN city ON (city_country_id = country_id) WHERE country_name = $1 ORDER BY city_id; ", [name], (arr) => {
        response.end(JSON.stringify(arr));
    }, () => {
        response.end(JSON.stringify({
            result: "DATABASE_ERROR",
        }));
    });
}
