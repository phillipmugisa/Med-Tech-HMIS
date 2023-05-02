function refreshView(page=1, view=null) {
    // this detects that views being used
    // then calls the render functions

    // user has to reclick recond so that the preview is updated
    if (document.querySelector(".preview-area")) {
        document.querySelector(".preview-area").innerHTML = "";
    }

    let url = window.location.href
    if (url.includes("patients")) {
        return renderPatientData();
    }
    else if (url.includes("visits")) {
        return renderVisitData();
    }
    else if (url.includes("triage")) {
        return rendertriageData();
    }
    else if (url.includes("doctor")) {
        if (view === "visit_list") {
            return renderVisitData();
        }
    }
}

function createTableRows (parentElem, data, fields, listener) {
    data.map((record, i) => {
        const rowElem = document.createElement("tr");
        rowElem.dataset.row = i
        rowElem.dataset.record_db_id = record["id"]
        fields.map(field => {
            const cell = document.createElement("td");
            cell.dataset.value = field
            if (field === "patient") {
                cell.textContent = record["patient"]["fullname"]
            }
            else if (field === "patientID") {
                cell.textContent = record["patient"]["patient_id"]
            }
            else {
                cell.textContent = record[field]
            }
            rowElem.appendChild(cell)
        })

        rowElem.addEventListener("click", (event) => {
            if(event.target.parentElement.tagName === "TR")
                listener(record)
        })

        parentElem.appendChild(rowElem)
    })
}

function renderPatientData(page=1) {
    return new Promise ((resolve, reject) => {
        // fetch data
        makeRequest(api_routes.patients_list, method="GET")
        .then(response => {
            const tableBody = document.querySelector("table#patientsTable tbody")
            // clear table body
            tableBody.innerHTML = "";
            createTableRows(tableBody, response.results, field=["patient_id", "fullname", "gender", "age", "visit", "created_on"], listener=loadPatientOnPreview)
        })
        .catch(response => {
            reject()
        })
        .finally(() => {
            $(`table#patientsTable`).DataTable()
            resolve()
        })
    })
}

function renderVisitData(page=1) {
    return new Promise ((resolve, reject) => {
        // fetch data
        makeRequest(api_routes.visits_list, method="GET")
        .then(response => {
            const tableBody = document.querySelector("table#visitsTable tbody")
            // clear table body
            tableBody.innerHTML = "";
            createTableRows(tableBody, response.results, field=["patientID", "patient", "category", "Speciality", "Doctor", "complete", "visit_date"], listener=loadVisitPreview)
        })
        .catch(response => {
            reject()
        })
        .finally(() => {
            $(`table#visitsTable`).DataTable()
            resolve()
        })
    })
}

function rendertriageData(page=1) {
    return new Promise ((resolve, reject) => {
        // fetch data
        makeRequest(api_routes.triage_list, method="GET")
        .then(response => {
            const tableBody = document.querySelector("table#triage_table tbody")
            // clear table body
            tableBody.innerHTML = "";
            createTableRows(tableBody, response, field=["patientID", "patient", "blood_pressure", "heart_rate", "respiratory_rate", "temperature", "created_on"], listener=loadTriagePreview)
        })
        .catch(response => {
            reject()
        })
        .finally(() => {
            $(`table#triage_table`).DataTable()
            resolve()
        })
    })
}