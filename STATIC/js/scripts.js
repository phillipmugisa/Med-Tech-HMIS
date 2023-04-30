document.addEventListener("DOMContentLoaded", () => {
    
    // section display
    // doctor view
    const section_togglers = document.querySelectorAll(".section-togglers")
    section_togglers.forEach(
        activator => activator.addEventListener("click", () => {
            let sectionToShow = document.querySelector(`#${activator.dataset.section}`)
            // console.log(sectionToShow)

            section_togglers.forEach(a=>{
                a.style.backgroundColor = "#1da1f2";
            })
            activator.style.backgroundColor = "hsl(203, 89%, 40%)";
            
            // close open modals
            let openSections = document.querySelectorAll(".variable-section.inview");
            openSections.forEach(section => section.classList.remove("inview"))

            sectionToShow.classList.add("inview")
        })
    )

    const section_part_toggler = document.querySelectorAll(".section-part-toggler")
    section_part_toggler.forEach(
        activator => activator.addEventListener("click", () => {
            let sectionToShow = document.querySelector(`#${activator.dataset.section}`)
            // console.log('Testing..' ,sectionToShow)
            
            // close open modals
            let openSections = document.querySelectorAll(".variable-section-part.inview");
            openSections.forEach(section => section.classList.remove("inview"))

            sectionToShow.classList.add("inview")
        })
    )

    // for selecting tests
    function createSelectedTestElem(test_id) {
        const elem = document.createElement("li");
        elem.dataset.testId = test_id;
        elem.innerHTML = `
            <h4 class="test_name">Malaria A</h4>
            <p class="test_description">Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi ex nostrum, necessitatibus corporis non quos?</p>
            <span class="action"><i class="fa fa-trash"></i></span>
        `
        elem.querySelector(".action").addEventListener("click", () => {
            elem.parentNode.removeChild(elem);
        })
        return elem
    }

    const request_tests = document.querySelectorAll("#request-test-list li")
    request_tests.forEach(test => test.addEventListener("click", () => {
        const selectedTestArea = document.querySelector("#selected_tests ul")
        console.log(selectedTestArea.querySelectorAll(`li[data-test-id="${test.dataset.testId}"]`))
        if (selectedTestArea.querySelectorAll(`li[data-test-id="${test.dataset.testId}"]`).length > 0)
            return;

        let selected_test_elem = createSelectedTestElem(test.dataset.testId);
        selectedTestArea.appendChild(selected_test_elem)
    }))
})