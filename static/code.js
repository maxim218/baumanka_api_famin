"use strict";

function sendPost(urlParam, bodyParam, callback) {
    const url = urlParam.toString();
    const r = new XMLHttpRequest();
    r.open("POST", url, true);
    r.setRequestHeader("Content-Type","application/json;charset=UTF-8");
    r.send(bodyParam.toString());
    r.onreadystatechange = function() {
        if(r.readyState === 4 && r.status === 200) {
            const answer = r.responseText;
            callback(answer.toString());
        }
    }
}

window.onload = function() {
    document.getElementById("mainBtn").onclick = function() {
        const arr = document.getElementsByClassName('fieldClass');
        const obj = {};
        for(let i = 0; i < arr.length; i++) {
            const id = arr[i].id.toString();
            obj[id] = arr[i].value.toString();
        }
        const url = document.getElementById("myForm").action;
        sendPost(url, JSON.stringify(obj), (ans) => {
            alert(ans);
        });
    }
}
