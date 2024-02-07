var currentVisitState = new State(null);
var currentPatientState = new State(null);
document.querySelectorAll(".section-togglers:not(#assigned_patients_toggler)")
    .forEach(elem => {
        elem.disabled = true;
        elem.classList.add("disabled")
    })

function createAllergyElem(id= null, name="", comment="") {
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
    elem.querySelector(".allergy_name").value = name;
    elem.querySelector(".allergy_comment").value = comment;
    if (id ==null) {
        elem.dataset.newRecord = true;
    }
    else {
        elem.dataset.allergyId = id;
    }

    elem.querySelector(".allergy_name").addEventListener("keydown", () => {
        if (elem.parentElement.lastChild == elem){
            elem.parentElement.appendChild(createAllergyElem())
        }
    })
    return elem
}

function refreshDoctorAllergieslist() {

    let allergies_form = document.querySelector("#allergies_form_area")
    allergies_form.innerHTML = ""

    // fetch allergies
    makeRequest(`/api/allergy/${currentPatientState.state.patient_id}/patient/`, method="GET")
    .then(response => {
        response.forEach(record => {
            allergies_form.appendChild(createAllergyElem(id=record.id, name=record.name, comment=record.comment))
        })
    })
    

    if (allergies_form && allergies_form.querySelectorAll(".addable-form-area").length < 1){
        allergies_form.appendChild(createAllergyElem())
    }

    // scroll to the bottom
    // allergies_form.querySelectorAll(".addable-form-area").scrollTo({bottom: 0})
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
                .addEventListener("click", () => refreshDoctorAllergieslist())
            })
        })
        .catch(response => {
        // ERROR: prompt reload
        })
    }))
})

document.querySelector("#general_doctor_toggler")
    .addEventListener("click", () => {
        document.querySelector("#sp_triage").click()
        // fetch triage data

        const showTriage = (data) =>  {
            displayTriageFormData(data, document.querySelector(".variable-section-part#triage"))
            let triage_form = document.querySelector("#triage_form")
            triage_form.dataset.triage = data.id
            triage_form.dataset.visit = data.visit
            document.querySelector("#triage_date").textContent = new Date(data.updated_on).toLocaleString()
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

document.querySelector("#clinical_findings_toggler")
    .addEventListener("click", () => {
        document.querySelector("#general_findings_activator").click()

        const showGeneralFindings = (data) =>  {
            document.querySelector("#presenting_complaints").value = data['presenting_complaints']
            document.querySelector("#clinical_notes").value = data['clinical_notes']
            document.querySelector("#rohs").value = data['rohs']
            document.querySelector("#psh").value = data['psh']
            document.querySelector("#poh").value = data['poh']
            document.querySelector("#cvs").value = data['cvs']
            document.querySelector("#general_appearance").value = data['general_appearance']
            document.querySelector("#respiratory").value = data['respiratory']
            document.querySelector("#ent").value = data['ent']
            document.querySelector("#abdomen_and_Gut").value = data['abdomen_and_Gut']
            document.querySelector("#cns").value = data['cns']
            document.querySelector("#eye").value = data['eye']
            document.querySelector("#muscular_skeletal").value = data['muscular_skeletal']
            document.querySelector("#skin").value = data['skin']
            document.querySelector("#pv_pr").value = data['pv_pr']
            document.querySelector("#psychological_status").value = data['psychological_status']
            document.querySelector("#provisional_status").value = data['provisional_status']
            document.querySelector("#treatment_plan").value = data['treatment_plan']

            let general_findings_form = document.querySelector("#general_findings_form")
            general_findings_form.dataset.general_finding = data.id
            // general_findings_form.dataset.general_finding = data.visit
            document.querySelector("#current_cf_date").textContent = new Date(data.updated_on).toLocaleString()
        }

        // fetch previous records
        makeRequest(`/api/generalfindings/${currentPatientState.state.patient_id}/patient/`, method="GET")
        .then(response => {
            let currentIdx = 0
            showGeneralFindings(response[currentIdx])
            document.querySelector("#previous_clinical_finding")
                .addEventListener("click", e => {
                    e.preventDefault()
                    if (currentIdx > 0){
                        currentIdx--
                        showGeneralFindings(response[currentIdx])
                    }
                })
            document.querySelector("#next_clinical_finding")
                .addEventListener("click", e => {
                    e.preventDefault()
                    if (currentIdx < response.length - 1){
                        currentIdx++
                        showGeneralFindings(response[currentIdx])
                    }
                })
        })
        .catch(response => {
            // ERROR: prompt reload
        })

        // saving
        document.querySelector("#general_findings_form")
            .addEventListener("submit", e => {
                e.preventDefault()
                if (e.target != document.querySelector("#save_clinical_finding")) {
                    return;
                }
                saveGeneralFindings()
            })

        document.querySelector("#save_clinical_finding")
            .addEventListener("click", e => {
                e.preventDefault()
                saveGeneralFindings()
            })

        function saveGeneralFindings() {

            presenting_complaints = document.querySelector("#presenting_complaints")
            clinical_notes = document.querySelector("#clinical_notes")
            rohs = document.querySelector("#rohs")
            psh = document.querySelector("#psh")
            poh = document.querySelector("#poh")
            cvs = document.querySelector("#cvs")
            general_appearance = document.querySelector("#general_appearance")
            respiratory = document.querySelector("#respiratory")
            ent = document.querySelector("#ent")
            abdomen_and_Gut = document.querySelector("#abdomen_and_Gut")
            cns = document.querySelector("#cns")
            eye = document.querySelector("#eye")
            muscular_skeletal = document.querySelector("#muscular_skeletal")
            skin = document.querySelector("#skin")
            pv_pr = document.querySelector("#pv_pr")
            psychological_status = document.querySelector("#psychological_status")
            provisional_status = document.querySelector("#provisional_status")
            treatment_plan = document.querySelector("#treatment_plan")

            let formNotEmpty = false;
            document.querySelectorAll("#general_findings_form input, #general_findings_form textarea")
                .forEach(elem => {
                    if (elem.value != "" || elem.value != undefined) {
                        formNotEmpty = true
                        return
                    }
                })
            
            if (!formNotEmpty) {return}

            let general_findings_form = document.querySelector("#general_findings_form")
            let general_findings_data = {
                "presenting_complaints" : presenting_complaints.value,
                "clinical_notes" : clinical_notes.value,
                "rohs" : rohs.value,
                "psh" : psh.value,
                "poh" : poh.value,
                "cvs" : cvs.value,
                "general_appearance" : general_appearance.value,
                "respiratory" : respiratory.value,
                "ent" : ent.value,
                "abdomen_and_Gut" : abdomen_and_Gut.value,
                "cns" : cns.value,
                "eye" : eye.value,
                "muscular_skeletal" : muscular_skeletal.value,
                "skin" : skin.value,
                "pv_pr" : pv_pr.value,
                "psychological_status" : psychological_status.value,
                "provisional_status" : provisional_status.value,
            }         
            
            // get current Visit finding
            makeRequest(`/api/generalfindings/${currentVisitState.state.id}/visit/`, method="GET")
            .then(response => {
                if (response.length > 0) {
                    if (general_findings_form.dataset.general_finding != response[0].id) {
                        return
                    }
                    else {
                        makeRequest(`/api/generalfindings/${general_findings_form.dataset.general_finding}/update/`, method="PATCH", data=general_findings_data)
                        .then(response => {
                            // show success message
                            alert("Edited")
                        })
                        .catch(response => {
                            // render error
                        })
                    }
                }
                else {
                    general_findings_data["visit"] = currentVisitState.state.id
                    makeRequest(`/api/generalfindings/create/`, method="POST", data=general_findings_data)
                    .then(response => {
                        // show success message
                        alert("Created")
                    })
                    .catch(response => {
                        // render error
                    })
                }
            })

        }
    })


document.querySelector("#paedeatrics_activator")
    .addEventListener("click", () => {

        const showPaedeatrics = (data) =>  {
            document.querySelector("#paedeatric_notes").value = data['notes']

            let paedeatrics_form = document.querySelector("#paedeatrics_form")
            paedeatrics_form.dataset.note = data.id
            document.querySelector("#current_pd_date").textContent = new Date(data.updated_on).toLocaleString()
        }

        // fetch previous records
        makeRequest(`/api/paedeatricnotes/${currentPatientState.state.patient_id}/patient/`, method="GET")
        .then(response => {
            let currentIdx = 0
            showPaedeatrics(response[currentIdx])
            document.querySelector("#previous_clinical_finding")
                .addEventListener("click", e => {
                    e.preventDefault()
                    if (currentIdx > 0){
                        currentIdx--
                        showPaedeatrics(response[currentIdx])
                    }
                })
            document.querySelector("#next_clinical_finding")
                .addEventListener("click", e => {
                    e.preventDefault()
                    if (currentIdx < response.length - 1){
                        currentIdx++
                        showPaedeatrics(response[currentIdx])
                    }
                })
        })
        .catch(response => {
            // ERROR: prompt reload
        })

        // saving
        document.querySelector("#paedeatrics_form")
            .addEventListener("submit", e => {
                e.preventDefault()
                if (e.target != document.querySelector("#save_paedeatrics")) {
                    return;
                }
                savePaedeatrics()
            })

        document.querySelector("#save_paedeatrics")
            .addEventListener("click", e => {
                e.preventDefault()
                savePaedeatrics()
            })

        function savePaedeatrics() {

            paedeatric_notes = document.querySelector("#paedeatric_notes")

            let formNotEmpty = false;
            document.querySelectorAll("#paedeatrics_form input, #paedeatrics_form textarea")
                .forEach(elem => {
                    if (elem.value != "" || elem.value != undefined) {
                        formNotEmpty = true
                        return
                    }
                })
            
            if (!formNotEmpty) {return}

            let paedeatrics_form = document.querySelector("#paedeatrics_form")
            let paedeatrics_data = {
                "notes" : paedeatric_notes.value,
            }         
            
            // get current Visit note
            // console.log(currentVisitState.state.id)
            makeRequest(`/api/paedeatricnotes/${currentVisitState.state.id}/visit/`, method="GET")
            .then(response => {
                if (response.length > 0) {
                    if (paedeatrics_form.dataset.note != response[0].id) {
                        return
                    }
                    else {
                        makeRequest(`/api/paedeatricnotes/${paedeatrics_form.dataset.note}/update/`, method="PATCH", data=paedeatrics_data)
                        .then(response => {
                            // show success message
                            alert("Edited")
                        })
                        .catch(response => {
                            // render error
                        })
                    }
                }
                else {
                    paedeatrics_data["visit"] = currentVisitState.state.id
                    makeRequest(`/api/paedeatricnotes/create/`, method="POST", data=paedeatrics_data)
                    .then(response => {
                        // show success message
                        alert("Created")
                    })
                    .catch(response => {
                        // render error
                    })
                }
            })

        }
    })

document.querySelector("#gyn_activator")
    .addEventListener("click", () => {

        const showGyn = (data) =>  {
            document.querySelector("#gyn_notes").value = data['notes']

            let gyn_form = document.querySelector("#gyn_form")
            gyn_form.dataset.note = data.id
            document.querySelector("#current_pd_date").textContent = new Date(data.updated_on).toLocaleString()
        }

        // fetch previous records
        makeRequest(`/api/gynnotes/${currentPatientState.state.patient_id}/patient/`, method="GET")
        .then(response => {
            let currentIdx = 0
            showGyn(response[currentIdx])
            document.querySelector("#previous_clinical_finding")
                .addEventListener("click", e => {
                    e.preventDefault()
                    if (currentIdx > 0){
                        currentIdx--
                        showGyn(response[currentIdx])
                    }
                })
            document.querySelector("#next_clinical_finding")
                .addEventListener("click", e => {
                    e.preventDefault()
                    if (currentIdx < response.length - 1){
                        currentIdx++
                        showGyn(response[currentIdx])
                    }
                })
        })
        .catch(response => {
            // ERROR: prompt reload
        })

        // saving
        document.querySelector("#gyn_form")
            .addEventListener("submit", e => {
                e.preventDefault()
                if (e.target != document.querySelector("#save_gyn")) {
                    return;
                }
                saveGyn()
            })

        document.querySelector("#save_gyn")
            .addEventListener("click", e => {
                e.preventDefault()
                saveGyn()
            })

        function saveGyn() {

            gyn_notes = document.querySelector("#gyn_notes")

            let formNotEmpty = false;
            document.querySelectorAll("#gyn_form input, #gyn_form textarea")
                .forEach(elem => {
                    if (elem.value != "" || elem.value != undefined) {
                        formNotEmpty = true
                        return
                    }
                })
            
            if (!formNotEmpty) {return}

            let gyn_form = document.querySelector("#gyn_form")
            let gyn_data = {
                "notes" : gyn_notes.value,
            }         
            
            // get current Visit note
            makeRequest(`/api/gynnotes/${currentVisitState.state.id}/visit/`, method="GET")
            .then(response => {
                if (response.length > 0) {
                    if (gyn_form.dataset.note != response[0].id) {
                        return
                    }
                    else {
                        makeRequest(`/api/gynnotes/${gyn_form.dataset.note}/update/`, method="PATCH", data=gyn_data)
                        .then(response => {
                            // show success message
                            alert("Edited")
                        })
                        .catch(response => {
                            // render error
                        })
                    }
                }
                else {
                    gyn_data["visit"] = currentVisitState.state.id
                    makeRequest(`/api/gynnotes/create/`, method="POST", data=gyn_data)
                    .then(response => {
                        // show success message
                        alert("Created")
                    })
                    .catch(response => {
                        // render error
                    })
                }
            })

        }
    })