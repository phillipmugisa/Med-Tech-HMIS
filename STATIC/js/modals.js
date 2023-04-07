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
    // close open modals
    console.log(typeof patient, patient);
}


function triggerCreateVisitModal(){
    document.querySelector("#create_patient_modal_activator").click();
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

