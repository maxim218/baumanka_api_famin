"use strict";

import clear from "./clear.js";
import addNewCountry from "./addNewCountry.js";
import addNewCity from "./addNewCity.js";
import addNewAirport from "./addNewAirport.js"
import getTableContent from "./getTableContent.js";
import addNewMan from "./addNewMan.js";

export default function route(app) {
    app.get('/api/database/clear', function(request, response) {
        clear(request, response);
    });

    app.get('/api/database/:table/select', function(request, response) {
        getTableContent(request, response);
    });

    app.post('/api/database/country/add', function(request, response) {
        addNewCountry(request, response);
    });

    app.post('/api/database/city/add', function(request, response) {
        addNewCity(request, response);
    });

    app.post('/api/database/airport/add', function(request, response) {
        addNewAirport(request, response);
    });

    app.post('/api/database/man/add', function(request, response) {
        addNewMan(request, response);
    });
}
