document.querySelector(".section-togglers#laboratory")
.addEventListener("click", () => {
    var labRequestState;

    // display lab results by default
    document.querySelector("#lab_results_activator").click()

    function onLabRequestSelect(record) {
        document.querySelector("#create_lab_request_activator").click()
        resetRequestCreationView()
        document.querySelector("#place_request_activator").dataset.action = "edit"

        labRequestState = new State({
          request: record.id,
          category: record.category.name,
          visit_id: record.visit_id,
          visit_pk: record.visit,
          selectedTests : []
        });

        // fetch assigned tests
        makeRequest(url=`/api/lab/tests/${record.id}/request/`, method="GET")
            .then(response => {
                for (let record of response) {
                    makeRequest(url=`/api/lab/tests/${record.test}`, method="GET")
                    .then(response => {
                        let test = {...response, ...record}

                        let elem = createSelectedTestElem(test)
                        const selectedTestArea = document.querySelector("#selected_tests ul")
                        if (selectedTestArea.querySelectorAll(`li[data-test-id="${test.id}"]`).length > 0)
                            return;

                        selectedTestArea.appendChild(elem)
                        labRequestState.selectedTests.push(test)
                        document.querySelector("#test_count").textContent = labRequestState.selectedTests.length
                    })
                }
            })
        
        // labRequestState.selectedTests.push(test)
        
        // select test search field by default
        document.querySelector("#doctor_search_lab_tests_field").focus()
        document.querySelector("#doctor_search_lab_tests_field").closest("form").reset()
        makeRequest(url=`/api/lab/tests/laboratory/`, method="GET")
          .then(response => {
            renderTestList(response)
          })
        
    }

      // fetch this patient lab requests
    renderLabRequestData(page=1, url=`/api/lab/requests/${currentPatientState.state.patient_id}/patient/`, tableId="doctor_lab_requests", listener=onLabRequestSelect)

      // for selecting tests
    function createSelectedTestElem(test) {
          const elem = document.createElement("li");
          elem.dataset.testId = test.id;
          elem.innerHTML = `
            <h4 class="test_name">${test.name}</h4>
            <p class="test_description">${test.description}</p>
            <p class="test_description">Normal Range:  ${test.dafault_range}</p>
            <div class="test_price">
              <span>${test.currency}</span>
              <input type="number" value="${test.price}" class="test_price_value"/>
            </div>
              <span class="action"><i class="fa fa-trash"></i></span>
          `
          elem.querySelector(".test_price_value").addEventListener("change", e => {
            let edited = {...test}
            edited.price = e.target.value
            labRequestState.selectedTests = [
              ...labRequestState.selectedTests.filter(_test => _test.id != test.id),
              edited
            ]
          })
          elem.querySelector(".action").addEventListener("click", () => {
              elem.parentNode.removeChild(elem);
              labRequestState.selectedTests = labRequestState.selectedTests.filter(_test => _test.id != test.id)
              document.querySelector("#test_count").textContent = labRequestState.selectedTests.length
          })
          return elem
    }
      
    function renderTestList(response) {
        let list = document.querySelector("#request-test-list")
        list.innerHTML = ""
        response.forEach(test => {
          const elem = document.createElement("li")
          elem.dataset.testId = test.id
          elem.innerHTML = `
            <h4 class="test_name">${test.name}</h4>
            <p class="test_description">${test.description}</p>
            <p class="test_description">Normal Range:  ${test.dafault_range}</p>
            <p class="test_price">${test.currency} ${test.price}</p>
          `
          list.appendChild(elem)
          elem.addEventListener("click", () => {
            const selectedTestArea = document.querySelector("#selected_tests ul")
            if (selectedTestArea.querySelectorAll(`li[data-test-id="${test.id}"]`).length > 0)
                return;
  
            let selected_test_elem = createSelectedTestElem(test);
            selectedTestArea.appendChild(selected_test_elem)
            
            labRequestState.selectedTests.push(test)
            document.querySelector("#test_count").textContent = labRequestState.selectedTests.length
          })
        });
    }
  
    function handleRequestCreation() {
        document.querySelector("#place_request_activator").dataset.action = "create"
        labRequestState = new State({
          category: "Laboratory",
          visit_id: currentVisitState.state.visit_id,
          visit_pk: currentVisitState.state.id,
          selectedTests : []
        });
        
        // select test search field by default
        document.querySelector("#doctor_search_lab_tests_field").focus()
        document.querySelector("#doctor_search_lab_tests_field").closest("form").reset()
        makeRequest(url=`/api/lab/tests/laboratory/`, method="GET")
          .then(response => {
            renderTestList(response)
          })
     }
  
    document.querySelector("#create_lab_request_activator")
        .addEventListener("click", handleRequestCreation)
      
    document.querySelector("#place_request_activator")
        .addEventListener("click", () => {
          // add confirmation dialog
          console.log("Please Confirm This action")

          if (document.querySelector("#place_request_activator").dataset.action === "create") {
            makeRequest(`/api/lab/requests/create/`, method="POST", data=labRequestState)
            .then(response => {
  
              resetRequestCreationView()
              document.querySelector("#lab_results_activator").click()
              renderLabRequestData(page=1, url=`/api/lab/requests/${currentPatientState.state.patient_id}/patient/`, tableId="doctor_lab_requests", listener=onLabRequestSelect)
            })
          }
          else {
            console.log(document.querySelector("#place_request_activator").dataset.action)
            makeRequest(`/api/lab/requests/${labRequestState.request}/update/`, method="PATCH", data=labRequestState)
            .then(response => {
              alert("Edited")
  
              renderLabRequestData(page=1, url=`/api/lab/requests/${currentPatientState.state.patient_id}/patient/`, tableId="doctor_lab_requests", listener=onLabRequestSelect)
            })
          }
          
        })

    function resetRequestCreationView() {
        labRequestState = null;
        document.querySelector("#selected_tests ul").innerHTML = ""
        document.querySelector("#test_count").textContent = 0
    }
  
      // document.querySelector("#lab_results_activator")
      //   .addEventListener("click", () => {
      //       if (labRequestState.selectedTests.length > 0) {
      //         alert("Complete Request Creation.")
      //         return;
      //       }
      //     })

    document.querySelector("#doctor_search_lab_tests_field").closest("form")
      .addEventListener("submit", e => e.preventDefault())
      
    // doctor searches for test
    document.querySelector("#doctor_search_lab_tests_field")
        .addEventListener("keyup", e => {
            makeRequest(url=`/api/lab/tests/laboratory/?s=${e.target.value}`, method="GET")
            .then(response => {
                renderTestList(response)
            })
        })
})