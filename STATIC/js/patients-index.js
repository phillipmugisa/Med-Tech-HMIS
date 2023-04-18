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
    <div class="cta_area">
        <button onclick="triggerEditPatientModal({id:${parseInt(patient.id)}})"  class="modal-activators">Edit Detials</button>
        <button onclick="triggerCreateVisitModal()" class="modal-activators">Create Visit</button>
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


  // Set up your table
  let table = $('#data-table').DataTable();

  // Signout
  const signoutBtn = document.querySelector('.fa-sign-out');

  signoutBtn.addEventListener('click', (event) => {
    window.location.href = "../auth/index.html";
  });



  // Billing
  // Display field for insurance company
  // When insurance is selected as the payment mode

  const billingMethodsDropdown = document.querySelector("#billing_methods");
  billingMethodsDropdown.addEventListener("change", function() {
    const selectedOption = billingMethodsDropdown.value;
    if(selectedOption === "insurance"){
      // The more elegant way causes the billing mode field to overflow
      document.querySelectorAll(".to_billing_company")[0].classList.remove("visibility-hidden");
      document.querySelectorAll(".to_billing_company")[1].classList.remove("visibility-hidden");
    }else{
      // The more elegant way causes the billing mode field to overflow
      document.querySelectorAll(".to_billing_company")[0].classList.add("visibility-hidden");
      document.querySelectorAll(".to_billing_company")[1].classList.add("visibility-hidden");
    }
});

