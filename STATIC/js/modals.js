document.addEventListener("DOMContentLoaded", () => {

    // declare modal activators
    const modal_activators = document.querySelectorAll(".modal-activators")
    modal_activators.forEach(
        activator => activator.addEventListener("click", () => {
            let modalToOpen = document.querySelector(`#${activator.dataset.modal}`);
            
            // close open modals
            let openModals = document.querySelectorAll(".modal.inview");
            openModals.forEach(modal => modal.classList.remove("inview"));

            modalToOpen.classList.add("inview");

            modalToOpen.querySelector("img.cancel").addEventListener("click", () => {
                modalToOpen.classList.remove("inview");
            })
        })
    )

})


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

    document.querySelector("#firstName").value = patient.firstname
    document.querySelector("#middleName").value = patient.middlename
    document.querySelector("#lastName").value = patient.lastname
    document.querySelector("#NIN").value = patient.nin
    document.querySelector("#age").value = patient.age
    document.querySelector("#dateOfBirth").value = patient.date_of_birth
    document.querySelector("#gender").value = patient.gender
    document.querySelector("#phoneNumber").value = patient.telnumber
    document.querySelector("#AltNumber").value = patient.alttelnumber
    document.querySelector("#email").value = patient.email
    document.querySelector("#address").value = patient.address
    document.querySelector("#patient_id").value = patient.patient_id

    // create nok of kin data
    makeRequest(`${api_routes.nok_list}${patient.id}/`, method="GET")
    .then(response => {
        document.querySelector("#NOK_firstName").value = response.firstname
        // setting nok id
        document.querySelector("#NOK_firstName").dataset.nokid = response.id
        document.querySelector("#NOK_middleName").value = response.middlename
        document.querySelector("#NOK_lastName").value = response.lastname
        document.querySelector("#NOK_relationship").value = response.relationship
        document.querySelector("#NOK_nin").value = response.nin
        document.querySelector("#NOK_phoneNumber").value = response.telnumber
        document.querySelector("#NOK_Gender").value = response.gender
        document.querySelector("#NOK_address").value = response.address

        // the modal action is changed to edit to show that its edit mode
        document.querySelector("#create_patient_modal").dataset.action = "edit"
        // document.querySelector("#create_patient_modal #modal_title").textContent = "Edit Patient"
    })
    .catch(response => {
        // render error
    })
    .finally(() => $(`table#patientsTable`).DataTable())

}


function triggerCreateVisitModal(){
    let modalToOpen = document.querySelector(`#create_visit_modal`);
            
    // close open modals
    let openModals = document.querySelectorAll(".modal.inview");
    openModals.forEach(modal => modal.classList.remove("inview"));

    modalToOpen.classList.add("inview");

    modalToOpen.querySelector("img.cancel").addEventListener("click", () => {
        modalToOpen.classList.remove("inview");
    })
    
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

