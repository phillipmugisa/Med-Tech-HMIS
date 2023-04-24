// Clear user on preview
const clearUserOnPreview = (user) => {
    const previewArea = document.querySelector("#user-preview");
    const previewContent = "";
    previewArea.innerHTML = previewContent;

  }
  // On page load, clear preview
  clearUserOnPreview();

  // Load user on preview
  const loadUserOnPreview = (user) => {
    const previewArea = document.querySelector("#user-preview");
    const previewContent = `
    <div class="img-wrapper">
        <img src="../../STATIC/images/user.png" alt="">
    </div>
    <div class="details">
        <div class="detail-group">
            <p class="part-title">Staff No.:</p>
            <p class="part-content">${user.id}</p>
        </div>
        <div class="detail-group">
            <p class="part-title">Name:</p>
            <p class="part-content">${user.name}</p>
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
            <p class="part-title">Gender:</p>
            <p class="part-content">${user.gender}</p>
        </div>
        <div class="detail-group">
            <p class="part-title">Designition:</p>
            <p class="part-content">${user.designition}</p>
        </div>
        <div class="detail-group">
            <p class="part-title">Acc Status:</p>
            <p class="part-content">${user.accountStatus}</p>
        </div>
    </div>
    <div class="cta_area">
        <button onclick="triggerEditUserModal({id:${parseInt(user.id)}})"  class="modal-activators">Update Staff</button>
        <button onclick="triggerUserRolesModal({id:${parseInt(user.id)}})"  class="modal-activators">User Roles</button>
    </div>
    `;
    previewArea.innerHTML = previewContent;

  }

  // Change user on prview
  const userRows = document.querySelector("tbody").querySelectorAll("tr");
  userRows.forEach(userRow => userRow.addEventListener("click", (event) => {
    if(event.target.parentElement.tagName === "TR"){
      const user = {
        id:event.target.parentElement.querySelectorAll("td")[0].textContent,
        name:event.target.parentElement.querySelectorAll("td")[1].textContent,
        gender:event.target.parentElement.querySelectorAll("td")[2].textContent,
        designition:event.target.parentElement.querySelectorAll("td")[3].textContent,
        accountStatus:event.target.parentElement.querySelectorAll("td")[4].textContent
      }
    loadUserOnPreview(user);
    }
  }));


  // Set up your table
  let table = $('#data-table').DataTable();

  // Signout
  const signoutBtn = document.querySelector('.fa-sign-out');

  signoutBtn.addEventListener('click', (event) => {
    window.location.href = "../auth/index.html";
  });