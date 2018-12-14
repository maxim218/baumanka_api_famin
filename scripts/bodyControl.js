"use strict";

export default function bodyControl(request, response, callback) {
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

