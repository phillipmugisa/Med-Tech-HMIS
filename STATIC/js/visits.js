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
    <div class="cta_area">
        <button  class="modal-activators" id="edit_patient_modal_activator" data-modal="create_patient_modal">Edit Detials</button>
        <button class="modal-activators" id="create_visit_modal_activator" data-modal="create_visit_modal">Create Visit</button>
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

  // Signout
  const signoutBtn = document.querySelector('.fa-sign-out');

  signoutBtn.addEventListener('click', (event) => {
    window.location.href = "../auth/index.html";
  });
