function refreshView() {
    // this detects that views being used
    // then calls the render functions

    let url = window.location.href
    if (url.includes("patients")) {
        renderPatientData();
    }
    else if (url.includes("visits")) {
        renderVisitData();
    }
}

function createTableRows (parentElem, data, fields, listener) {
    data.map((record, i) => {
        const rowElem = document.createElement("tr");
        rowElem.dataset.row = i

        fields.map(field => {
            const cell = document.createElement("td");
            cell.dataset.value = field
            cell.textContent = record[field]
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
    // fetch data
    makeRequest(api_routes.patients_list, method="GET")
    .then(response => {
        const tableBody = document.querySelector("table#patientsTable tbody")
        // clear table body
        tableBody.innerHTML = "";
        createTableRows(tableBody, response.results, field=["patient_id", "fullname", "gender", "age", "visit", "created_on"], listener=loadPatientOnPreview)
    })
    .catch(response => {
        // render error
    })
    .finally(() => $(`table#patientsTable`).DataTable())
}

function renderVisitData(page=1) {
    // fetch data
    makeRequest(api_routes.visits_list, method="GET")
    .then(response => {
        const tableBody = document.querySelector("table#visitsTable tbody")
        // clear table body
        tableBody.innerHTML = "";
        createTableRows(tableBody, response.results, field=["patient_id", "category", "Speciality", "Doctor", "complete", "visit_date"], listener=loadVisitPreview)
    })
    .catch(response => {
        // render error
    })
    // .finally(() => $(`table#visitsTable`).DataTable())
}