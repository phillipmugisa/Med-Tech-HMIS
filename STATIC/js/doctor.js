var currentVisitState = new State(null);
var currentPatientState = new State(null);
document.querySelectorAll(".section-togglers:not(#assigned_patients_toggler)")
    .forEach(elem => {
    elem.disabled = true;
    elem.classList.add("disabled")
    })

function createAllergyElem() {
    const elem = document.createElement("div")
    elem.className = "addable-form-area"
    elem.innerHTML = `
    <div class="form-group">
        <label for="">Name</label>
        <input type="text" class="allergy_name input"/>
    </div>
    <div class="form-group">
        <label for="">Comments</label>
        <textarea cols="100%" rows="3" class="allergy_comment input"></textarea>
    </div>
    `
    elem.querySelector(".allergy_name").addEventListener("keydown", () => {
        if (elem.parentElement.lastChild == elem){
            elem.parentElement.appendChild(createAllergyElem())
        }
    })
    return elem
}

// load data
refreshView(1, "visit_list")
.then(() => {
    document.querySelectorAll("#visitsTable tbody tr")
    .forEach(elem => elem.addEventListener("click", () => {
        // fetch visit
        makeRequest(`/api/visits/${elem.dataset.record_db_id}`, method="GET")
        .then(response => {
        currentVisitState.setState(response)
        document.querySelectorAll(".section-togglers:not(#assigned_patients_toggler)")
        .forEach(elem => {
            elem.disabled = false;
            elem.classList.remove("disabled")
        })
        
        // fetch patient being worked on
        makeRequest(`/api/visit/${response.id}/patient/`, method="GET")
        .then(response => {
            currentPatientState.setState(response)
            document.querySelector("#general_doctor_toggler").click()
            
            document.querySelector("#sp_allergies")
            .addEventListener("click", () => {
                let allergies_form = document.querySelector("#allergies_form_area")
                if (allergies_form && allergies_form.querySelectorAll(".addable-form-area").length < 1){
                    allergies_form.appendChild(createAllergyElem())
                }
            })
        })
        })
        .catch(response => {
        // ERROR: prompt reload
        })
    }))
})

document.querySelector("#general_doctor_toggler")
    .addEventListener("click", () => {
    // fetch triage data

    const showTriage = (data) =>  {
        displayTriageFormData(data, document.querySelector(".variable-section-part#triage"))
        let triage_form = document.querySelector("#triage_form")
        triage_form.dataset.triage = data.id
        triage_form.dataset.visit = data.visit
        document.querySelector("#triage_date").textContent = data.updated_on
    }
    
    makeRequest(`/api/triage/${currentPatientState.state.patient_id}/patient/`, method="GET")
    .then(response => {
        let currentTriageIdx = 0
        showTriage(response[currentTriageIdx])
        document.querySelector("#previous_triage")
        .addEventListener("click", e => {
            e.preventDefault()
            if (currentTriageIdx > 0){
            currentTriageIdx--
            showTriage(response[currentTriageIdx])
            }
        })
        document.querySelector("#next_triage")
        .addEventListener("click", e => {
            e.preventDefault()
            if (currentTriageIdx < response.length - 1){
            currentTriageIdx++
            showTriage(response[currentTriageIdx])
            }
        })
    })
    .catch(response => {
        // ERROR: prompt reload
    })
})