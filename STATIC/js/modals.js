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

function triggerEditPatientModal(patient){
    // close open modals
    let openModals = document.querySelectorAll(".modal.inview");
    openModals.forEach(modal => modal.classList.remove("inview"));

    // open the modal
    const modalToOpen = document.querySelector("#create_patient_modal");
    modalToOpen.querySelector(".modal-header").querySelector("h3").textContent = "Edit Patient";
    modalToOpen.classList.add("inview");
    console.log(typeof patient, patient);

    modalToOpen.querySelector("img.cancel").addEventListener("click", () => {
        modalToOpen.classList.remove("inview");
    });
}


function triggerCreateVisitModal(){
    // close open modals
    let openModals = document.querySelectorAll(".modal.inview");
    openModals.forEach(modal => modal.classList.remove("inview"));

    // open the modal
    const modalToOpen = document.querySelector("#create_visit_modal");
    modalToOpen.classList.add("inview");

    modalToOpen.querySelector("img.cancel").addEventListener("click", () => {
        modalToOpen.classList.remove("inview");
    });
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