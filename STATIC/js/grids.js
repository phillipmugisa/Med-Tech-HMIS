document.addEventListener("DOMContentLoaded", () => {

    // declare grid activators
    const grid_activators = document.querySelectorAll(".grid-activators")
    grid_activators.forEach(
        activator => activator.addEventListener("click", () => {
            let gridToOpen = document.querySelector(`#${activator.dataset.table}`);
            console.log(10)
            
            // remove grids  from view
            let openGrids = document.querySelectorAll(".data-grid.display-block");
            openGrids.forEach(grid => grid.classList.remove("display-block"));

            gridToOpen.classList.add("display-block");
        })
    )

})
