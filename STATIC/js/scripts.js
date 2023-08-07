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


})