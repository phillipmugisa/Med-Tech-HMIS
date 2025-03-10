// Load patient on preview

const backend_url = "http://localhost:8000"

const loadPatientOnPreview = (patient) => {
    const main = document.querySelector("main")
    main.classList.add("split")
    let previewArea = document.querySelector(".preview-area");
    let previewContent = `
    <div class="img-wrapper">
        <img src="${backend_url}/static/images/user.png" alt="">
    </div>
    <div class="details" id="preview_detials">
        <div class="detail-group">
            <p class="part-title">Patient:</p>
            <p class="part-content">${patient.patient_id}</p>
        </div>
        <div class="detail-group">
            <p class="part-title">Full Name:</p>
            <p class="part-content" id="preview_patient_name">${patient.fullname}</p>
        </div>
        <div class="detail-group">
            <p class="part-title">NIN:</p>
            <p class="part-content">${patient.nin}</p>
        </div>
        <div class="detail-group">
            <p class="part-title">Phone No:</p>
            <p class="part-content">${patient.telnumber}</p>
        </div>
        <div class="detail-group">
            <p class="part-title">Address:</p>
            <p class="part-content">${patient.address}</p>
        </div>
        <div class="detail-group">
            <p class="part-title">Gender:</p>
            <p class="part-content">${patient.gender}</p>
        </div>
        <div class="detail-group">
            <p class="part-title">Age:</p>
            <p class="part-content">${patient.age}</p>
        </div>
    </div>
    <div class="cta_area">
        <button  class="modal-activators" id="edit_patient_modal_activator" data-modal="create_patient_modal">Edit Detials</button>
        <button class="modal-activators" id="create_visit_modal_activator" data-modal="create_visit_modal">Create Visit</button>
    </div>
    `;
    previewArea.innerHTML = previewContent

    previewArea.querySelector("#edit_patient_modal_activator")
        .addEventListener("click", () => triggerEditPatientModal(patient))

        
    previewArea.querySelector("#create_visit_modal_activator")
        .addEventListener("click", () => triggerCreateVisitModal(patient))
}


const loadVisitPreview = (visit) => {
    const main = document.querySelector("main")
    main.classList.add("split")
    let previewArea = document.querySelector(".preview-area");
    let previewContent = `
    <div class="img-wrapper">
        <img src="${backend_url}/static/images/user.png" alt="">
    </div>
    <div class="details" id="preview_detials">
        <div class="detail-group">
            <p class="part-title">Patient:</p>
            <p class="part-content">${visit.patient.patient_id}</p>
        </div>
        <div class="detail-group">
            <p class="part-title">Visit:</p>
            <p class="part-content">${visit.visit_id}</p>
        </div>
        <div class="detail-group">
            <p class="part-title">Fullname:</p>
            <p class="part-content">${visit.patient.fullname}</p>
        </div>
        <div class="detail-group">
            <p class="part-title">Nin:</p>
            <p class="part-content">${visit.patient.nin}</p>
        </div>
        <div class="detail-group">
            <p class="part-title">Category</p>
            <p class="part-content" id="preview_patient_name">${visit.category.name}</p>
        </div>
        <div class="detail-group">
            <p class="part-title">Doctor:</p>
            <p class="part-content">${visit.Doctor}</p>
        </div>
        <div class="detail-group">
            <p class="part-title">Speciality:</p>
            <p class="part-content">${visit.Speciality}</p>
        </div>
        <div class="detail-group">
            <p class="part-title">Complete:</p>
            <p class="part-content">${visit.complete}</p>
        </div>
    </div>
    <div class="cta_area">
        <button class="modal-activators" id="edit_visit_modal_activator" data-modal="create_patient_modal">Edit Details</button>
    </div
    `;
    previewArea.innerHTML = previewContent

    previewArea.querySelector("#edit_visit_modal_activator")
        .addEventListener("click", () => triggerCreateVisitModal(visit, edit=true))
}

const loadTriagePreview = (triage) => {
    const main = document.querySelector("main")
    main.classList.add("split")
    let previewArea = document.querySelector(".preview-area");
    let previewContent = `
    <div class="img-wrapper">
        <img src="${backend_url}/static/images/user.png" alt="">
    </div>
    <div class="details" id="preview_detials">
        <div class="detail-group">
            <p class="part-title">Patient:</p>
            <p class="part-content">${triage.patient_id ? triage.patient_id : triage.patient.patient_id}</p>
        </div>
        <div class="detail-group">
            <p class="part-title">Fullname:</p>
            <p class="part-content">${triage.patient.fullname}</p>
        </div>
        <div class="detail-group">
            <p class="part-title">Nin:</p>
            <p class="part-content">${triage.patient.nin}</p>
        </div>
        <div class="detail-group">
            <p class="part-title">Blood Pressure</p>
            <p class="part-content" id="preview_patient_name">${triage.blood_pressure}</p>
        </div>
        <div class="detail-group">
            <p class="part-title">Heart Rate:</p>
            <p class="part-content">${triage.heart_rate}</p>
        </div>
        <div class="detail-group">
            <p class="part-title">Respiratory Rate:</p>
            <p class="part-content">${triage.respiratory_rate}</p>
        </div>
        <div class="detail-group">
            <p class="part-title">Temperature:</p>
            <p class="part-content">${triage.temperature}</p>
        </div>
        <div class="detail-group">
            <p class="part-title">Updated On:</p>
            <p class="part-content">${new Date(triage.updated_on).toLocaleString()}</p>
        </div>
    </div>
    <div class="cta_area">
        <button class="modal-activators" id="edit_visit_modal_activator" data-modal="create_patient_modal">Edit Details</button>
    </div
    `;
    previewArea.innerHTML = previewContent

    previewArea.querySelector("#edit_visit_modal_activator")
        .addEventListener("click", () => triggerCreateTriageModal(triage, edit=true))
}