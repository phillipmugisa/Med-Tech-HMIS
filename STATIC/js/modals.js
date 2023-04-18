document.addEventListener("DOMContentLoaded", () => {

    // declare modal activators
    const modal_activators = document.querySelectorAll(".modal-activators")

    modal_activators.forEach(
        activator => activator.addEventListener("click", () => openModal(activator))
    )


    // Billing
    // Display field for insurance company
    // When insurance is selected as the payment mode

    const billingMethodsDropdown = document.querySelector("#billing_methods");
    if (billingMethodsDropdown) {
        billingMethodsDropdown.addEventListener("change", function() {
            const selectedOption = billingMethodsDropdown.value;
            if(selectedOption === "insurance"){
                // The more elegant way causes the billing mode field to overflow
                document.querySelectorAll(".to_billing_company")[0].classList.remove("visibility-hidden");
                document.querySelectorAll(".to_billing_company")[1].classList.remove("visibility-hidden");
            }else{
                // The more elegant way causes the billing mode field to overflow
                document.querySelectorAll(".to_billing_company")[0].classList.add("visibility-hidden");
                document.querySelectorAll(".to_billing_company")[1].classList.add("visibility-hidden");
            }
        });
    }
})

function openModal(activator) {
    let modalToOpen = document.querySelector(`#${activator.dataset.modal}`);
        
    // close open modals
    let openModals = document.querySelectorAll(".modal.inview");
    openModals.forEach(modal => modal.classList.remove("inview"));

    modalToOpen.classList.add("inview");
    modalToOpen.dataset.action = "create"

    modalToOpen.querySelector("img.cancel").addEventListener("click", () => {
        modalToOpen.querySelectorAll("form")
            .forEach(form => form.reset())
        modalToOpen.classList.remove("inview");
    })
}

function triggerEditUserModal(user){
    // close open modals
    let openModals = document.querySelectorAll(".modal.inview");
    openModals.forEach(modal => modal.classList.remove("inview"));

    // open the modal
    const modalToOpen = document.querySelector("#create_new_user_modal");
    modalToOpen.querySelector(".modal-header").querySelector("h3").textContent = "Update Existing Staff";
    modalToOpen.classList.add("inview");
    console.log(typeof user, user);

    modalToOpen.querySelector("img.cancel").addEventListener("click", () => {
        modalToOpen.querySelector(".modal-header").querySelector("h3").textContent = "Register New Staff";
        modalToOpen.classList.remove("inview");
    });
}

function triggerUserRolesModal(user){
    // close open modals
    let openModals = document.querySelectorAll(".modal.inview");
    openModals.forEach(modal => modal.classList.remove("inview"));

    // open the modal
    const modalToOpen = document.querySelector("#create_user_roles_modal");
    // modalToOpen.querySelector(".modal-header").querySelector("h3").textContent = "Update User Roles";
    modalToOpen.classList.add("inview");
    console.log(typeof user, user);

    modalToOpen.querySelector("img.cancel").addEventListener("click", () => {
        // modalToOpen.querySelector(".modal-header").querySelector("h3").textContent = "Create User Roles";
        modalToOpen.classList.remove("inview");
    });
}

function triggerEditPatientModal(patient){
    document.querySelector("#create_patient_modal_activator").click();

    const create_patient_modal = document.querySelector("#create_patient_modal");

    // the modal action is changed to edit to show that its edit mode
    create_patient_modal.dataset.action = "edit"
    // document.querySelector("#create_patient_modal #modal_title").textContent = "Edit Patient"

    create_patient_modal.querySelector("#firstName").value = patient.firstname
    create_patient_modal.querySelector("#middleName").value = patient.middlename
    create_patient_modal.querySelector("#lastName").value = patient.lastname
    create_patient_modal.querySelector("#NIN").value = patient.nin
    create_patient_modal.querySelector("#age").value = patient.age
    create_patient_modal.querySelector("#dateOfBirth").value = new Date(patient.date_of_birth)
    create_patient_modal.querySelector("#gender").value = patient.gender
    create_patient_modal.querySelector("#phoneNumber").value = patient.telnumber
    create_patient_modal.querySelector("#AltNumber").value = patient.alttelnumber
    create_patient_modal.querySelector("#email").value = patient.email
    create_patient_modal.querySelector("#address").value = patient.address
    create_patient_modal.querySelector("#patient_id").value = patient.patient_id

    // create nok of kin data
    makeRequest(`${api_routes.nok_list}${patient.id}/`, method="GET")
    .then(response => {
        create_patient_modal.querySelector("#NOK_firstName").value = response.firstname
        // setting nok id
        create_patient_modal.querySelector("#NOK_firstName").dataset.nokid = response.id
        create_patient_modal.querySelector("#NOK_middleName").value = response.middlename
        create_patient_modal.querySelector("#NOK_lastName").value = response.lastname
        create_patient_modal.querySelector("#NOK_relationship").value = response.relationship
        create_patient_modal.querySelector("#NOK_nin").value = response.nin
        create_patient_modal.querySelector("#NOK_phoneNumber").value = response.telnumber
        create_patient_modal.querySelector("#NOK_Gender").value = response.gender
        create_patient_modal.querySelector("#NOK_address").value = response.address
    })
    .catch(response => {
        // render error
    })
    .finally(() => $(`table#patientsTable`).DataTable())

}

function getPatientData() {
    // this function opens a modal in which a user can search for and select a patient
    // return: patient data
}

function triggerCreateVisitModal(data, edit=false){
    openModal(document.querySelector("#create_visit_modal_activator"))
    const create_visit_modal = document.querySelector("#create_visit_modal");

    if (!data) {
      
        if (create_visit_modal.dataset.action == "create" && (create_visit_modal.querySelector("#patient_id").value != undefined || create_visit_modal.querySelector("#patient_id").value != "")) {
            let load_patient_activator = document.querySelector("#load_patient_activator")
            load_patient_activator.style.display = "grid";
            create_visit_modal.querySelector("#patient_id").style.display = "none";
            create_visit_modal.querySelector("#patient_id_label").style.display = "none";
            load_patient_activator.addEventListener("click", () => {
                data = getPatientData()
                triggerCreateVisitModal(data)
            })
          }
    }

    if (edit ==true) {
        create_visit_modal.dataset.action = "edit"
        
        create_visit_modal.dataset.visit = data.id
        create_visit_modal.querySelector("#visit_date").value = new Date(data.visit_date)
        create_visit_modal.querySelector("#visit_doctor").value = data.doctor
        create_visit_modal.querySelector("#visit_specialty").value = data.speciality
        create_visit_modal.querySelector("#visit_category").value = data.category
        
        patient = data.patient
    }
    else {
        create_visit_modal.dataset.action = "create"
        patient = data
    }

    create_visit_modal.querySelector("#firstName").value = patient.firstname
    create_visit_modal.querySelector("#middleName").value = patient.middlename
    create_visit_modal.querySelector("#lastName").value = patient.lastname
    create_visit_modal.querySelector("#NIN").value = patient.nin
    create_visit_modal.querySelector("#age").value = patient.age
    create_visit_modal.querySelector("#dateOfBirth").value = new Date(patient.date_of_birth)
    create_visit_modal.querySelector("#gender").value = patient.gender
    create_visit_modal.querySelector("#patient_id").value = patient.patient_id
    // setting patient id
    create_visit_modal.querySelector("#firstName").dataset.pid = patient.id
}

function triggerCreateTriageModal(){
    // close open modals
    let openModals = document.querySelectorAll(".modal.inview");
    openModals.forEach(modal => modal.classList.remove("inview"));

    // open the modal
    const modalToOpen = document.querySelector("#create_triage_modal");
    modalToOpen.classList.add("inview");

    modalToOpen.querySelector("img.cancel").addEventListener("click", () => {
        modalToOpen.classList.remove("inview");
    });
}