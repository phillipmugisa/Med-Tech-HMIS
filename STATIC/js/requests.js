const api_routes = {
    "patients_list": "/api/patients/",
    "nok_list": "/api/nextOfKin/",
}

function removeEmpty(obj) {
    Object.keys(obj).forEach(key => {
        if (obj[key] && typeof obj[key] === 'object') {
        removeEmpty(obj[key]);
        } else if (obj[key] == null || obj[key] === '') {
        delete obj[key];
        }
    });
    return obj;
}

async function makeRequest (url, method, data={}, access_token=null) {
    const backend_url = `http://localhost:8000`;
    let requestData = {
        method: method,
        mode: "same-origin",
        cache: "no-cache",
        credentials: 'same-origin'
        // "headers" : {
        //     Authorization: "JWT " + localStorage.getItem("ext_access_token"),
        // }
    };


    if (method == "POST" || method == "PUT" || method == "PATCH") {
        requestData["body"] = JSON.stringify(removeEmpty(data));
        requestData["headers"] = {
            Accept: "application/json",
            "Content-Type": "application/json"
        }
    }

    const response = await fetch(`${backend_url}${url}`, requestData);
    if (response.status >= 200 && response.status <= 399) {
        return await response.json();
    }
    else {
        throw new Error(response);
    }
}