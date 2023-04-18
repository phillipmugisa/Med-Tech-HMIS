// Load patient on preview

const backend_url = "http://localhost:8000"

const loadPatientOnPreview = (patient) => {
    const previewArea = document.querySelector("#patient-preview");
    const previewContent = `
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

