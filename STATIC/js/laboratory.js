const sectionTabContents = document.querySelectorAll(".section-tabs-content");

      const sectionTabs = document.querySelectorAll(".section-tab");
      sectionTabs.forEach((sectionTab, key) => {
        sectionTab.addEventListener("click", (event) => {
          sectionTabs.forEach((sectionTab) => {
            if (sectionTab.classList.contains("current")) {
              sectionTab.classList.remove("current");
            }
          });
          sectionTabContents.forEach((sectionTabContent) => {
            if (!sectionTabContent.classList.contains("content-hidden")) {
              sectionTabContent.classList.add("content-hidden");
            }
          });
          sectionTab.classList.add("current");
          sectionTabContents[key].classList.remove("content-hidden");
        });
      });