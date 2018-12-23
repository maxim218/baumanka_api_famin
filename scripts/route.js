"use strict";

import clear from "./clear.js";
import addNewCountry from "./addNewCountry.js";
import addNewCity from "./addNewCity.js";
import addNewAirport from "./addNewAirport.js"
import getTableContent from "./getTableContent.js";
import addNewMan from "./addNewMan.js";
import addNewTicket from "./addNewTicket.js";
import getManInfo from "./getManInfo.js";
import addPair from "./addPair.js"
import getPairInfo from "./getPairInfo.js";
import getCountryByCityName from "./getCountryByCityName.js";
import getAllCitiesOfCountryByName from "./getAllCitiesOfCountryByName.js";

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

    app.post('/api/database/ticket/add', function(request, response) {
        addNewTicket(request, response);
    });

    app.get('/api/database/man/:id/get', function(request, response) {
        getManInfo(request, response);
    });

    app.post('/api/database/pair/add', function(request, response) {
        addPair(request, response);
    });

    app.get('/api/database/pair/:id/get', function(request, response) {
        getPairInfo(request, response);
    });

    app.get('/api/database/get_country_by_city_name', function(request, response) {
        getCountryByCityName(request, response);
    });

    app.get('/api/database/get_all_cities_of_country_by_name', function(request, response) {
        getAllCitiesOfCountryByName(request, response);
    });
}
