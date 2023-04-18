 // Clear insurance company on preview
 const clearInsuranceCompanyOnPreview = (company) => {
    const previewArea = document.querySelector("#insurance-company-preview");
    const previewContent = "";
    previewArea.innerHTML = previewContent;

  }
  // On page load, clear preview
  clearInsuranceCompanyOnPreview();

  // Load insurance company on preview
  const loadInsuranceCompanyOnPreview = (company) => {
    const previewArea = document.querySelector("#insurance-company-preview");
    const previewContent = `
    <div class="img-wrapper">
        <img src="../../STATIC/images/icea-logo.png" alt="">
    </div>
    <div class="details">
        <div class="detail-group">
            <p class="part-title">Company:</p>
            <p class="part-content">${company.name}</p>
        </div>
        <div class="detail-group">
            <p class="part-title">Represen..:</p>
            <p class="part-content">${company.designition}</p>
        </div>
        <div class="detail-group">
            <p class="part-title">Contact:</p>
            <p class="part-content">+256728463968</p>
        </div>
        <div class="detail-group">
            <p class="part-title">Website:</p>
            <p class="part-content">${company.gender}</p>
        </div>
    </div>
    <div class="cta_area">
        <button onclick="triggerEditInsuranceCompanyModal({id:${parseInt(company.id)}})"  class="modal-activators">Update Company</button>
    </div>
    `;
    previewArea.innerHTML = previewContent;

  }

  // Change company on prview
  const companyRows = document.querySelector("tbody").querySelectorAll("tr");
  companyRows.forEach(companyRow => companyRow.addEventListener("click", (event) => {
    if(event.target.parentElement.tagName === "TR"){
      const insuranceCompany = {
        id:event.target.parentElement.querySelectorAll("td")[0].textContent,
        name:event.target.parentElement.querySelectorAll("td")[1].textContent,
        gender:event.target.parentElement.querySelectorAll("td")[2].textContent,
        designition:event.target.parentElement.querySelectorAll("td")[3].textContent,
        accountStatus:event.target.parentElement.querySelectorAll("td")[4].textContent
      }
    loadInsuranceCompanyOnPreview(insuranceCompany);
    }
  }));


  // Set up your table
  let table01 = $('#data-table-01').DataTable();

  let table02 = $('#data-table-02').DataTable();

  // Signout
  const signoutBtn = document.querySelector('.fa-sign-out');

  signoutBtn.addEventListener('click', (event) => {
    window.location.href = "../auth/index.html";
  });