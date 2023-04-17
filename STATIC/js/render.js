function createTableRows (parentElem, data, fields) {
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
                loadPatientOnPreview(record)
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
        createTableRows(tableBody, response.results, field=["patient_id", "fullname", "gender", "age", "visit", "created_on"])
    })
    .catch(response => {
        // render error
    })
    .finally(() => $(`table#patientsTable`).DataTable())
}
