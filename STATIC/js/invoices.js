// Clear patient on preview
const clearPatientOnPreview = (patient) => {
    const previewArea = document.querySelector("#patient-preview");
    const previewContent = "";
    previewArea.innerHTML = previewContent;

  }
  // On page load, clear preview
  clearPatientOnPreview();

  // Load patient on preview
  const loadPatientOnPreview = (patient) => {
  const previewArea = document.querySelector("#patient-preview");
  const previewContent = `
  <div class="img-wrapper">
      <img src="../../STATIC/images/user.png" alt="">
  </div>
  <div class="details">
      <div class="detail-group">
          <p class="part-title">Patient No.:</p>
          <p class="part-content">${patient.id}</p>
      </div>
      <div class="detail-group">
          <p class="part-title">Name:</p>
          <p class="part-content">${patient.name}</p>
      </div>
      <div class="detail-group">
          <p class="part-title">NIN:</p>
          <p class="part-content">CM2REK234423MFC</p>
      </div>
      <div class="detail-group">
          <p class="part-title">Phone No:</p>
          <p class="part-content">+256728463968</p>
      </div>
      <div class="detail-group">
          <p class="part-title">Birth Place:</p>
          <p class="part-content">Wakiso</p>
      </div>
      <div class="detail-group">
          <p class="part-title">Gender:</p>
          <p class="part-content">${patient.gender}</p>
      </div>
      <div class="detail-group">
          <p class="part-title">Age:</p>
          <p class="part-content">${patient.age}</p>
      </div>
  </div>
  `;
  previewArea.innerHTML = previewContent;

}

// Change patient on prview
const patientRows = document.querySelector("tbody").querySelectorAll("tr");
patientRows.forEach(patientRow => patientRow.addEventListener("click", (event) => {
  if(event.target.parentElement.tagName === "TR"){
    const patient = {
      id:event.target.parentElement.querySelectorAll("td")[0].textContent,
      name:event.target.parentElement.querySelectorAll("td")[1].textContent,
      age:event.target.parentElement.querySelectorAll("td")[3].textContent,
      visit:event.target.parentElement.querySelectorAll("td")[4].textContent,
      gender:event.target.parentElement.querySelectorAll("td")[2].textContent
    }
  loadPatientOnPreview(patient);
  }
}))


    // Set up search table
    let table = $('#data-table-search-patient').DataTable();

    // Set up your table
    let table01 = $('#data-table-01').DataTable();
    let table02 = $('#data-table-02').DataTable();
    let table03 = $('#data-table-03').DataTable();

    // Extend dataTables search
    $.fn.dataTable.ext.search.push(
        function(settings, data, dataIndex) {
            var min = $('#from-date').val();
            var max = $('#to-date').val();
            var createdAt = data[3] || 0; // Our date column in the table
            if ((min == "" || max == "") || (moment(createdAt).isSameOrAfter(min) && moment(createdAt).isSameOrBefore(max))) {
                return true;
            }
            return false;
        }
    );

    // Re-draw the table when the a date range filter changes
    $('.date-range-filter-01').change(function() {
        table01.draw();
    });

    // Re-draw the table when the a date range filter changes
    $('.date-range-filter-02').change(function() {
        table02.draw();
    });

    // Re-draw the table when the a date range filter changes
    $('.date-range-filter-03').change(function() {
        table03.draw();
    });

    // Table rows
    const tableRows = document.querySelectorAll("tr");
    tableRows.forEach((tableRow) => {
        tableRow.addEventListener("click", handleTableRowClick);
    });

    function handleTableRowClick(event){
        const row = event.target.parentElement;
        // console.log(row)
        // Ignore the search patient table
        if(!row.classList.contains("search-patient-row")){
            if(row.classList.contains("even") || row.classList.contains("odd")){
                // console.log(row);
                // Pass ID to the modal
                // Or pass all the content for editing
                triggerEditInvoiceModal(row);
            }
        }
        // Handle search patient table here
        else if(row.classList.contains("search-patient-row")){
            if(row.classList.contains("even") || row.classList.contains("odd")){
                // console.log(row.cells[0].textContent.trim());
                // const currentPatient = {
                //     firstName: row.cells[1].textContent.trim().split(" ")[0],
                //     middleName: row.cells[1].textContent.trim().split(" ")[1],
                //     lastName: row.cells[1].textContent.trim().split(" ")[2],
                // };
                // console.log(currentPatient);
                const form = document.querySelector("#patient-information");
                form.elements.firstName.value = row.cells[1].textContent.trim().split(" ")[0];
                form.elements.middleName.value = row.cells[1].textContent.trim().split(" ")[1];
                form.elements.lastName.value = row.cells[1].textContent.trim().split(" ")[2];
                form.elements.age.value = row.cells[3].textContent.trim();
            }
        }
    }

    // Print table
    function printDataTable(mTitle, table) {
        const title = document.createElement('h3');
        title.style.textDecoration = "underline";
        title.textContent = mTitle;
        const divToPrint = document.querySelector(`#data-table-${table}`);
        divToPrint.append(title);
        let htmlToPrint = '' +
            '<style type="text/css">' +
                'table {' +
                    'border-collapse:collapse;' +
                '}' +
                'table th, table td {' +
                    'border:1px solid #000;' +
                    'padding:0.5em;' +
                '}' +
            '</style>';
        htmlToPrint += divToPrint.outerHTML;
        const newWin = window.open("");
        newWin.document.write(htmlToPrint);
        newWin.print();
        newWin.close();
        title.textContent = "";
    }

    document.querySelector("#print-data-table-01").addEventListener('click', ()=> {
        printDataTable("All Invoices", '01');
    });


    document.querySelector("#print-data-table-02").addEventListener('click', ()=> {
        printDataTable("Insurance Company", '02');
    });

    document.querySelector("#print-data-table-03").addEventListener('click', ()=> {
        printDataTable("Account Company", '03');
    });


    // Export as CSV
    function downloadCSV(tableId, fileName) {
        const table = document.getElementById(tableId);
        const rows = table.querySelectorAll("tr");

        // Prepare a CSV file content string
        let csvContent = "data:text/csv;charset=utf-8,";

        // Loop through each row of the table
        rows.forEach(function(row) {
            const cells = row.querySelectorAll("td, th");
            const rowData = [];

            // Loop through each cell of the row
            cells.forEach(function(cell) {
            rowData.push('"' + cell.innerText.replace(/"/g, '""') + '"');
            });

            // Combine the row data into a CSV row and add it to the file content
            csvContent += rowData.join(",") + "\r\n";
        });

        // Create a download link and trigger the download
        const encodedUri = encodeURI(csvContent);
        const link = document.createElement("a");
        link.setAttribute("href", encodedUri);
        link.setAttribute("download", fileName);
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }

    document.querySelector("#export-data-table-01").addEventListener('click', ()=> {
        downloadCSV('data-table-01', "revenues")
    });


    document.querySelector("#export-data-table-02").addEventListener('click', ()=> {
        downloadCSV('data-table-02', "expenses")
    });

    document.querySelector("#export-data-table-03").addEventListener('click', ()=> {
        downloadCSV('data-table-03', "income")
    });


  // Add new invoice items
  function createNextRow(selectElement) {
    const tableRow = selectElement.parentElement.parentElement;
    const tableBody = tableRow.parentElement;
    const nextRow = document.createElement('tr');
    const nextRowSelect = document.createElement('select');
    const nextRowColumn1 = document.createElement('td');
    const nextRowColumn2 = document.createElement('td');
    const nextRowColumn3 = document.createElement('td');
    const deleteButton = document.createElement('button');

    // Add empty option
    nextRowSelect.appendChild(document.createElement('option'));

    // Add options from current row
    const currentRowOptions = tableRow.querySelectorAll('option');
    for (let i = 1; i < currentRowOptions.length; i++) {
      const optionValue = currentRowOptions[i].value;
      const optionPrice = currentRowOptions[i].dataset.price;
      const option = document.createElement('option');
      option.value = optionValue;
      option.dataset.price = optionPrice;
      option.textContent = optionValue;
      nextRowSelect.appendChild(option);
    }

    // Add event listener to new select element
    nextRowSelect.onchange = function() {
      const priceInput = this.parentElement.nextElementSibling.querySelector('input');
      const selectedOption = this.options[this.selectedIndex];
      priceInput.value = selectedOption.dataset.price;
      createNextRow(this);
    }

    // Add select and column to new row
    nextRowColumn1.appendChild(nextRowSelect);
    nextRow.appendChild(nextRowColumn1);

    // Add input field for price to new row
    const nextRowPrice = document.createElement('input');
    nextRowPrice.type = 'text';
    // nextRowPrice.readOnly = true;
    nextRowColumn2.appendChild(nextRowPrice);
    nextRow.appendChild(nextRowColumn2);

    // Add button for deleting row to new row
    deleteButton.textContent = 'Delete';
    deleteButton.onclick = function() {
      tableBody.removeChild(nextRow);
    }
    nextRowColumn3.appendChild(deleteButton);
    nextRow.appendChild(nextRowColumn3);

    // Add new row to table body
    tableBody.appendChild(nextRow);
  }
    
  // Signout
  const signoutBtn = document.querySelector('.fa-sign-out');

  signoutBtn.addEventListener('click', (event) => {
    window.location.href = "../auth/index.html";
  });

