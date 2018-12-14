/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, {
/******/ 				configurable: false,
/******/ 				enumerable: true,
/******/ 				get: getter
/******/ 			});
/******/ 		}
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = 3);
/******/ })
/************************************************************************/
/******/ ([
/* 0 */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (immutable) */ __webpack_exports__["a"] = makeQuery;
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__global_js__ = __webpack_require__(2);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__debug_js__ = __webpack_require__(6);





const params = {
    database: "base",
    user: "postgres",
    password: "12345",
    host: "localhost",
    port: 5432,
};

function createNewClient() {
    const pg = Object(__WEBPACK_IMPORTED_MODULE_0__global_js__["a" /* default */])().pg;
    return new pg.Client({
        user: params.user,
        host: params.host,
        database: params.database,
        password: params.password,
        port: params.port,
    });
}

function makeQuery(query, arr, callbackGood, callbackBad) {
    const client = createNewClient();
    client.connect();

    if(Object(__WEBPACK_IMPORTED_MODULE_1__debug_js__["a" /* default */])() === true) {
        console.log("   ");
        console.log(query);
        console.log("----------------------------------------");
    }

    client.query(query, arr, (err, res) => {
        client.end();

        if(!err) {
            callbackGood(res.rows);
        } else {
            callbackBad();
        }
    });
}


/***/ }),
/* 1 */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (immutable) */ __webpack_exports__["a"] = bodyControl;


function bodyControl(request, response, callback) {
    const bodyArr = [];
    request.on('data', (data) => {
        bodyArr.push(data.toString());
    }).on('end', () => {
        const bodyString = bodyArr.join("");
        try {
            const bodyObj = JSON.parse(bodyString.toString());
            callback(bodyObj);
        } catch(err) {
            response.end(JSON.stringify({
                result: "JSON_ERROR"
            }));
        }
    });
}



/***/ }),
/* 2 */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (immutable) */ __webpack_exports__["a"] = global;


const GLOBAL = {};

function global() {
    return GLOBAL;
}



/***/ }),
/* 3 */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__global_js__ = __webpack_require__(2);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__route_js__ = __webpack_require__(4);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__generate_js__ = __webpack_require__(14);
"use script";





const PORT = 5007;

function start() {
    let express = __webpack_require__(15);
    let app = express();

    let pg = __webpack_require__(16);
    Object(__WEBPACK_IMPORTED_MODULE_0__global_js__["a" /* default */])().pg = pg;

    let fs = __webpack_require__(17);
    Object(__WEBPACK_IMPORTED_MODULE_0__global_js__["a" /* default */])().fs = fs;

    app.use(function(req, res, next) {
        res.header("Cache-Control", "no-cache, no-store, must-revalidate");
        res.header("Access-Control-Allow-Origin", "*");
        res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
        next();
    });

    const port = parseInt(PORT);
    app.listen(port);
    console.log("    ");
    console.log("Server port: " + port);
    console.log("-----------------------------------");
    console.log("    ");

    Object(__WEBPACK_IMPORTED_MODULE_2__generate_js__["a" /* default */])("addCountry", ['country_name'], 'api/database/country/add');
    Object(__WEBPACK_IMPORTED_MODULE_2__generate_js__["a" /* default */])("addCity", ['city_name', 'city_country_id'], 'api/database/city/add');
    Object(__WEBPACK_IMPORTED_MODULE_2__generate_js__["a" /* default */])("addAirport", ['airport_name', 'airport_city_id'], 'api/database/airport/add');
    Object(__WEBPACK_IMPORTED_MODULE_2__generate_js__["a" /* default */])("addMan", ['man_fullname', 'man_city'], 'api/database/man/add');
    Object(__WEBPACK_IMPORTED_MODULE_2__generate_js__["a" /* default */])("addTicket", ['ticket_airport_a', 'ticket_airport_b', 'ticket_man_id'], 'api/database/ticket/add');

    Object(__WEBPACK_IMPORTED_MODULE_1__route_js__["a" /* default */])(app);
}

start();

function printNewLines() {
    console.log("    ");
    console.log("-----------------------------------");
    console.log("    ");
    console.log("System is ready to work ...");
    console.log("    ");
}

setTimeout(printNewLines, 4000);

/***/ }),
/* 4 */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (immutable) */ __webpack_exports__["a"] = route;
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__clear_js__ = __webpack_require__(5);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__addNewCountry_js__ = __webpack_require__(7);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__addNewCity_js__ = __webpack_require__(8);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__addNewAirport_js__ = __webpack_require__(9);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4__getTableContent_js__ = __webpack_require__(10);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_5__addNewMan_js__ = __webpack_require__(11);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_6__addNewTicket_js__ = __webpack_require__(12);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_7__getManInfo_js__ = __webpack_require__(13);











function route(app) {
    app.get('/api/database/clear', function(request, response) {
        Object(__WEBPACK_IMPORTED_MODULE_0__clear_js__["a" /* default */])(request, response);
    });

    app.get('/api/database/:table/select', function(request, response) {
        Object(__WEBPACK_IMPORTED_MODULE_4__getTableContent_js__["a" /* default */])(request, response);
    });

    app.post('/api/database/country/add', function(request, response) {
        Object(__WEBPACK_IMPORTED_MODULE_1__addNewCountry_js__["a" /* default */])(request, response);
    });

    app.post('/api/database/city/add', function(request, response) {
        Object(__WEBPACK_IMPORTED_MODULE_2__addNewCity_js__["a" /* default */])(request, response);
    });

    app.post('/api/database/airport/add', function(request, response) {
        Object(__WEBPACK_IMPORTED_MODULE_3__addNewAirport_js__["a" /* default */])(request, response);
    });

    app.post('/api/database/man/add', function(request, response) {
        Object(__WEBPACK_IMPORTED_MODULE_5__addNewMan_js__["a" /* default */])(request, response);
    });

    app.post('/api/database/ticket/add', function(request, response) {
        Object(__WEBPACK_IMPORTED_MODULE_6__addNewTicket_js__["a" /* default */])(request, response);
    });

    app.get('/api/database/man/:id/get', function(request, response) {
        Object(__WEBPACK_IMPORTED_MODULE_7__getManInfo_js__["a" /* default */])(request, response);
    });
}


/***/ }),
/* 5 */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (immutable) */ __webpack_exports__["a"] = clear;
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__global_js__ = __webpack_require__(2);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__makeQuery_js__ = __webpack_require__(0);





function clear(request, response) {
    const fs = Object(__WEBPACK_IMPORTED_MODULE_0__global_js__["a" /* default */])().fs;
    const sqlCode = fs.readFileSync('main.sql', 'utf8');
    Object(__WEBPACK_IMPORTED_MODULE_1__makeQuery_js__["a" /* default */])(sqlCode.toString(), [], () => {
        response.end(JSON.stringify({
            result: "INIT_DATABASE_OK"
        }));
     }, () => {
        throw new Error();
     });
}



/***/ }),
/* 6 */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (immutable) */ __webpack_exports__["a"] = debug;


const DEBUG = true;

function debug() {
    return DEBUG;
}


/***/ }),
/* 7 */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (immutable) */ __webpack_exports__["a"] = addNewCountry;
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__makeQuery_js__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__bodyControl__ = __webpack_require__(1);





function addNewCountry(request, response) {
    Object(__WEBPACK_IMPORTED_MODULE_1__bodyControl__["a" /* default */])(request, response, (body) => {
        Object(__WEBPACK_IMPORTED_MODULE_0__makeQuery_js__["a" /* default */])("INSERT INTO country (country_name) VALUES ($1) RETURNING *; ", [body.country_name], (arr) => {
            const result = arr[0];
            response.end(JSON.stringify(result));
        }, () => {
            response.end(JSON.stringify({
                result: "COUNTRY_ALREADY_EXISTS"
            }));
        });
    });
}



/***/ }),
/* 8 */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (immutable) */ __webpack_exports__["a"] = addNewCity;
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__makeQuery_js__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__bodyControl__ = __webpack_require__(1);





function addNewCity(request, response) {
    Object(__WEBPACK_IMPORTED_MODULE_1__bodyControl__["a" /* default */])(request, response, (body) => {
        Object(__WEBPACK_IMPORTED_MODULE_0__makeQuery_js__["a" /* default */])("INSERT INTO city (city_name, city_country_id) VALUES($1, $2) RETURNING *; ", [body.city_name, parseInt(body.city_country_id)], (arr) => {
            const result = arr[0];
            response.end(JSON.stringify(result));
        }, () => {
            response.end(JSON.stringify({
                result: "COUNTRY_NOT_FOUND",
            }));
        });
    });
}


/***/ }),
/* 9 */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (immutable) */ __webpack_exports__["a"] = addNewAirport;
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__makeQuery_js__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__bodyControl__ = __webpack_require__(1);





function addNewAirport(request, response) {
    Object(__WEBPACK_IMPORTED_MODULE_1__bodyControl__["a" /* default */])(request, response, (body) => {
        Object(__WEBPACK_IMPORTED_MODULE_0__makeQuery_js__["a" /* default */])("INSERT INTO airport (airport_name, airport_city_id) VALUES ($1, $2) RETURNING *; ", [body.airport_name, parseInt(body.airport_city_id)], (arr) => {
            const result = arr[0];
            response.end(JSON.stringify(result));
        }, () => {
            response.end(JSON.stringify({
                result: "CITY_NOT_FOUND",
            }));
        });
    });
}


/***/ }),
/* 10 */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (immutable) */ __webpack_exports__["a"] = getTableContent;
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__makeQuery_js__ = __webpack_require__(0);




function getTableContent(request, response) {
    const tableName = request.params.table.toString();
    const idName = tableName + "_id";
    const query = " SELECT * FROM " + tableName + " ORDER BY " + idName + " DESC; ";

    Object(__WEBPACK_IMPORTED_MODULE_0__makeQuery_js__["a" /* default */])(query, [], (arr) => {
        response.end(JSON.stringify(arr));
    }, () => {
        response.end(JSON.stringify({
            result: "TABLE_NOT_FOUND",
        }));
    });
}


/***/ }),
/* 11 */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (immutable) */ __webpack_exports__["a"] = addNewMan;
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__makeQuery_js__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__bodyControl__ = __webpack_require__(1);





function addNewMan(request, response) {
    Object(__WEBPACK_IMPORTED_MODULE_1__bodyControl__["a" /* default */])(request, response, (body) => {
        Object(__WEBPACK_IMPORTED_MODULE_0__makeQuery_js__["a" /* default */])("INSERT INTO man (man_fullname, man_city) VALUES ($1, $2) RETURNING *; ", [body.man_fullname, parseInt(body.man_city)], (arr) => {
            const answer = arr[0];
            response.end(JSON.stringify(answer));
        }, () => {
            response.end(JSON.stringify({
                result: "CITY_NOT_FOUND",
            }));
        });
    });
}


/***/ }),
/* 12 */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (immutable) */ __webpack_exports__["a"] = addNewTicket;
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__makeQuery_js__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__bodyControl_js__ = __webpack_require__(1);





function addNewTicket(request, response) {
    Object(__WEBPACK_IMPORTED_MODULE_1__bodyControl_js__["a" /* default */])(request, response, (body) => {
        const airA = parseInt(body.ticket_airport_a);
        const airB = parseInt(body.ticket_airport_b);
        const man = parseInt(body.ticket_man_id);
        const paramsArr = [
            airA,
            airB,
            man,
        ];
        Object(__WEBPACK_IMPORTED_MODULE_0__makeQuery_js__["a" /* default */])("INSERT INTO ticket (ticket_airport_a, ticket_airport_b, ticket_date, ticket_man_id) VALUES ($1, $2, NOW(), $3) RETURNING *; ", paramsArr, (arr) => {
            const result = arr[0];
            response.end(JSON.stringify(result));
        }, () => {
            response.end(JSON.stringify({
                result: "AIRPORT_OR_MAN_NOT_FOUND",
            }));
        });
    });
}


/***/ }),
/* 13 */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (immutable) */ __webpack_exports__["a"] = getManInfo;
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__makeQuery__ = __webpack_require__(0);


"use strict";

function getManInfo(request, response) {
    const id = request.params.id.toString();
    Object(__WEBPACK_IMPORTED_MODULE_0__makeQuery__["a" /* default */])("SELECT * FROM man INNER JOIN city ON (man_city = city_id) INNER JOIN country ON (city_country_id = country_id) WHERE man_id = $1 LIMIT 1; ", [parseInt(id)], (arr) => {
        response.end(JSON.stringify(arr));
    }, () => {
        response.end(JSON.stringify({
            result: "DATABASE_ERROR",
        }));
    });
}


/***/ }),
/* 14 */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (immutable) */ __webpack_exports__["a"] = generate;
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__global_js__ = __webpack_require__(2);




const URL = "http://localhost:5007/";

function generate(name, mass, url) {
    const fs = Object(__WEBPACK_IMPORTED_MODULE_0__global_js__["a" /* default */])().fs;

    let content = `<!doctype html>
        <html>
        <head>
            <style>
                .fieldClass {
                    margin-left: 15px;
                    padding: 7px;
                    width: 300px;
                }
            </style>
            <meta charset="UTF-8" />
            <title>${name}</title>
        </head>
        <body>
        <h1>${name}</h1>`;

    content += `<form id = "myForm" action = ${URL + url} method = 'POST'>`;
    
    for(let i = 0; i < mass.length; i++) {
        content += `<p>${mass[i]}</p>`;
        content += `<input type = "text" class = "fieldClass" spellcheck = "false" autocomplete = "off" id = ${mass[i]}>`;
        content += `<br>`;
    }

    content += `<br><input type = "button" value = "Send" id = "mainBtn">`;
    content += `</form>`;

    content += "<script src = './code.js'></script>"

    content += `</body>
        </html>`;

    fs.writeFile("./static/" + name + ".html", content, function(err) {
        console.log("Create " + "./static/" + name + ".html" + " OK");
    }); 
}

/***/ }),
/* 15 */
/***/ (function(module, exports) {

module.exports = require("express");

/***/ }),
/* 16 */
/***/ (function(module, exports) {

module.exports = require("pg");

/***/ }),
/* 17 */
/***/ (function(module, exports) {

module.exports = require("fs");

/***/ })
/******/ ]);