"use strict";

import global from "./global.js";

const URL = "http://localhost:5007/";

export default function generate(name, mass, url) {
    const fs = global().fs;

    let content = `<!doctype html>
        <html>
        <head>
            <style>
                .fieldClass {
                    margin-left: 15px;
                    padding: 7px;
                    width: 300px;
                }

                body {
                    background: #CCCCCC;
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