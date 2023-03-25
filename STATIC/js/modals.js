document.addEventListener("DOMContentLoaded", () => {

    // declare modal activators
    const modal_activators = document.querySelectorAll(".modal-activators")
    modal_activators.forEach(
        activator => activator.addEventListener("click", () => {
            let modalToOpen = document.querySelector(`#${activator.dataset.modal}`)
            
            // close open modals
            let openModals = document.querySelectorAll(".modal.inview");
            openModals.forEach(modal => modal.classList.remove("inview"))

            modalToOpen.classList.add("inview")

            modalToOpen.querySelector("img.cancel").addEventListener("click", () => {
                modalToOpen.classList.remove("inview")
            })
        })
    )

})