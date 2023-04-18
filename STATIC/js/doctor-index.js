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
            <p class="part-title">First Name:</p>
            <p class="part-content">${patient.name}</p>
        </div>
        <div class="detail-group">
            <p class="part-title">Last No.:</p>
            <p class="part-content">Muhumuza</p>
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
        age:event.target.parentElement.querySelectorAll("td")[2].textContent,
        visit:event.target.parentElement.querySelectorAll("td")[3].textContent,
        gender:event.target.parentElement.querySelectorAll("td")[4].textContent
      }
    console.log(patient);
    loadPatientOnPreview(patient);
    }
  }))

  // Set up your table
  let table = $('#data-table').DataTable();


  // Add new diagnosis items
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
    

  // Add new prescription items
  function createNextPrescriptionRow(selectElement) {
    const tableRow = selectElement.parentElement.parentElement;
    const tableBody = tableRow.parentElement;
    const nextRow = document.createElement('tr');
    const nextRowSelect = document.createElement('select');
    const nextRowColumn1 = document.createElement('td');
    const nextRowColumn2 = document.createElement('td');
    const nextRowColumn3 = document.createElement('td');
    const nextRowColumn4 = document.createElement('td');
    const nextRowColumn5 = document.createElement('td');
    const nextRowColumn6 = document.createElement('td');
    const nextRowColumn7 = document.createElement('td');
    const nextRowColumn8 = document.createElement('td');
    const nextRowColumn9 = document.createElement('td');
    const nextRowColumn10 = document.createElement('td');
    const nextRowColumn11 = document.createElement('td');
    const nextRowColumn12 = document.createElement('td');
    const deleteButton = document.createElement('button');

    // Add empty option
    nextRowSelect.appendChild(document.createElement('option'));

    // Add options from current row
    const currentRowOptions = tableRow.querySelectorAll('option');
    for (let i = 1; i < currentRowOptions.length; i++) {
      const optionValue = currentRowOptions[i].value;
      const option = document.createElement('option');
      option.value = optionValue;
      option.textContent = optionValue;
      nextRowSelect.appendChild(option);
    }

    // Add event listener to new select element
    nextRowSelect.onchange = function() {
      const selectedOption = this.options[this.selectedIndex];
      createNextPrescriptionRow(this);
    }

    // Add select and column to new row
    nextRowColumn1.appendChild(nextRowSelect);
    nextRow.appendChild(nextRowColumn1);

    // Add input field for dosage to new row
    const nextRowDosage = document.createElement('input');
    nextRowDosage.type = 'text';
    // nextRowDosage.readOnly = true;
    nextRowColumn2.appendChild(nextRowDosage);
    nextRow.appendChild(nextRowColumn2);


    // Add input field for duration to new row
    const nextRowDuration = document.createElement('input');
    nextRowDuration.type = 'text';
    // nextRowDuration.readOnly = true;
    nextRowColumn3.appendChild(nextRowDuration);
    nextRow.appendChild(nextRowColumn3);



    // Add input field for quantity of drug
    const nextRowQunatity = document.createElement('input');
    nextRowQunatity.type = 'text';
    // nextRowQunatity.readOnly = true;
    nextRowColumn4.appendChild(nextRowQunatity);
    nextRow.appendChild(nextRowColumn4);


    // Add input field for drug notes
    const nextRowNotes = document.createElement('input');
    nextRowNotes.type = 'text';
    // nextRowNotes.readOnly = true;
    nextRowColumn5.appendChild(nextRowNotes);
    nextRow.appendChild(nextRowColumn5);


    // Add input field for stock left
    const nextRowStockLeft = document.createElement('input');
    nextRowStockLeft.type = 'text';
    // nextRowStockLeft.readOnly = true;
    nextRowColumn6.appendChild(nextRowStockLeft);
    nextRow.appendChild(nextRowColumn6);

    // Add input field for prescribed qty
    const nextRowPrescribedQty = document.createElement('input');
    nextRowPrescribedQty.type = 'text';
    // nextRowPrescribedQty.readOnly = true;
    nextRowColumn7.appendChild(nextRowPrescribedQty);
    nextRow.appendChild(nextRowColumn7);

    // Add input field for measure
    const nextRowMeasure = document.createElement('input');
    nextRowMeasure.type = 'text';
    // nextRowMeasure.readOnly = true;
    nextRowColumn8.appendChild(nextRowMeasure);
    nextRow.appendChild(nextRowColumn8);

    // Add input field for price
    const nextRowPrice = document.createElement('input');
    nextRowPrice.type = 'text';
    // nextRowPrice.readOnly = true;
    nextRowColumn9.appendChild(nextRowPrice);
    nextRow.appendChild(nextRowColumn9);

    // Add input field for amount
    const nextRowAmount = document.createElement('input');
    nextRowAmount.type = 'text';
    // nextRowAmount.readOnly = true;
    nextRowColumn10.appendChild(nextRowAmount);
    nextRow.appendChild(nextRowColumn10);

    // Add input field for prescribed by
    const nextRowPrescribedBy = document.createElement('input');
    nextRowPrescribedBy.type = 'text';
    // nextRowPrescribedBy.readOnly = true;
    nextRowColumn11.appendChild(nextRowPrescribedBy);
    nextRow.appendChild(nextRowColumn11);

    // Add button for deleting row to new row
    deleteButton.textContent = 'Delete';
    deleteButton.onclick = function() {
      tableBody.removeChild(nextRow);
    }

    nextRowColumn12.appendChild(deleteButton);
    nextRow.appendChild(nextRowColumn12);

    // Add new row to table body
    tableBody.appendChild(nextRow);
  }
    

  // Signout
  const signoutBtn = document.querySelector('.fa-sign-out');

  signoutBtn.addEventListener('click', (event) => {
    window.location.href = "../auth/index.html";
  });